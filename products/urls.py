from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_lists, name='product-lists'),
    path('<category_slug>/', views.by_category, name='by-category'),
    path('<category_slug>/<product_slug>/', views.single_product, name='single-product'),
]