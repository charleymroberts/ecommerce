# Generated by Django 4.2.1 on 2023-09-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0002_alter_product_barcode_alter_product_categories_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="show_in_menu",
            field=models.BooleanField(default=True),
        ),
    ]
