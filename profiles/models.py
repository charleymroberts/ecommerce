from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    default_address = models.BooleanField(default=False)
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=100, blank=True, null=True)
    line_three = models.CharField(max_length=100, blank=True, null=True)
    town_city_or_area = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=8)

    def __str__(self):
        return self.line_one, self.postcode


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    loyalty_points = models.IntegerField()