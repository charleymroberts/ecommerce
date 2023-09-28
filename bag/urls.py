from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view-bag'),
    path('add/<product_id>/', views.add_to_bag, name='add-to-bag'),
    path('edit/<product_id>/', views.edit_bag, name='edit-bag'),
]
