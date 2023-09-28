from django import template


register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity


# this file copied from Boutique Ado walkthrough project


@register.filter(name="chilled_total")
def chilled_total(cool_box, total):
    return cool_box + total
