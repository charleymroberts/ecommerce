from .models import Category


def navbar(request):
    nav_categories = Category.objects.filter(
        parent__isnull=True, show_in_menu=True
    )

    context = {
        "nav_categories": nav_categories,
    }

    return context
