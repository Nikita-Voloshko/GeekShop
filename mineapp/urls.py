from django.urls import path

from mineapp.views import products

app_name = 'mineapp'
urlpatterns = [
    path('', products, name='index'),
    path('<int:id/>', products, name='products')
]
