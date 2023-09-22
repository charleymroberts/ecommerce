from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_account, name='my-account'),
    path('addresses/', views.addresses, name='addresses'),
    path('add-address/', views.add_address, name='add-address'),
]