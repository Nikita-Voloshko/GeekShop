from django.urls import path

from mineapp.views import productss, index

app_name = 'mineapp'
urlpatterns = [
    path('', index, name='index'),
    path('<int:category_id/>', productss, name='products'),
]
