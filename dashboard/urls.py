from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add-product'),
    path('view-products/', views.view_products, name='view-products'),
    path('edit-product/<product_slug>/', views.edit_product, name='edit-product'),
    path('add-brand/', views.add_brand, name='add-brand'),
    path('edit-brand/<brand_slug>/', views.edit_brand, name='edit-brand'),
    path('view-brands/', views.view_brands, name='view-brands'),
]