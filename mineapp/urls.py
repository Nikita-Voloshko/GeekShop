from django.urls import path

from mineapp.views import Product, index

app_name = 'mineapp'
urlpatterns = [
    path('', index, name='index'),
    path('<int:category_id/>', Product, name='products'),
]
