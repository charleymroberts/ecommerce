from django.urls import path
from . import views


urlpatterns = [
    path('brands/<brand_slug>/', views.brand, name='brand'),
    path('<category_slug>/', views.by_category, name='by-category'),
    path('<category_slug>/<product_slug>/',
         views.single_product, name='single-product'),
    path('', views.search_results, name='search-results'),
]
