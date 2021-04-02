from django.shortcuts import render
from mineapp.models import products, ProductCategory


# Create your views here.
def index(request):
    return render(request, 'mineapp/index.html')


def product(request, id=None):
    print(id)
    context = {
        'products': products.objects.all(),
        'categories':  ProductCategory.objects.all()
    }
    return render(request, 'mineapp/products.html', context)
