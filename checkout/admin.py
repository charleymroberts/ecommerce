from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "date",
        "full_name",
        "email",
        "line_one",
        "line_two",
        "line_three",
        "town_city_or_area",
        "county",
        "postcode",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
