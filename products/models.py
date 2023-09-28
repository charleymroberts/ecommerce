from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class VatRate(models.TextChoices):
    ZERO = "Z", _("Zero rated")
    STANDARD = "S", _("Standard rated")
    REDUCED = "R", _("Reduced rated")


class Category(models.Model):
    name = models.CharField(max_length=254)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
    )
    description = models.TextField()
    slug = models.SlugField(unique=True)
    show_in_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey("Brand", on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True)
    wholesale_price = models.DecimalField(max_digits=5, decimal_places=2)
    retail_price = models.DecimalField(max_digits=5, decimal_places=2)
    vat_rate = models.CharField(
        max_length=1,
        blank=False,
        choices=VatRate.choices,
        default=VatRate.ZERO,
    )
    barcode = models.CharField(
        max_length=50, unique=True, null=True, blank=True
    )
    ingredients = models.TextField(null=True, blank=True)
    nutrition_info = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_organic = models.BooleanField()
    is_glutenfree = models.BooleanField()
    liked_by = models.ManyToManyField(
        User, related_name="favourites", blank=True
    )
    categories = models.ManyToManyField(
        "Category", related_name="products", blank=True
    )

    def __str__(self):
        return self.name
