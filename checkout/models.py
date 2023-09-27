import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=100, blank=True, null=True)
    line_three = models.CharField(max_length=100, blank=True, null=True)
    town_city_or_area = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=8)
    date = models.DateTimeField(auto_now_add=True)
    cool_box_included = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        """
        Delivery costs
        """
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = 5
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        if self.cool_box_included:
            self.grand_total += settings.COOL_BOX
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.retail_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
