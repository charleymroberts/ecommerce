from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_account, name='my-account'),
    path('addresses/', views.addresses, name='addresses'),
    path('add-address/', views.add_address, name='add-address'),
    path('edit-address/<address_id>/', views.edit_address, name='edit-address'),
    path('delete-address/<address_id>/', views.delete_address, name='delete-address'),
    path('set-default-address/', views.set_default_address, name='set-default-address'),
]