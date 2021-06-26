from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basket.models import Basket
from mineapp.models import Product
# Create your views here.


def basket_add(request, product_id=None):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user)

    if baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity = + 1
        basket.save
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first
        basket.quantity = + 1
        basket.save
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
