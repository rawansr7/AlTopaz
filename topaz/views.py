from django.shortcuts import render
from product.models import Product


def home(request):
    products_objs = Product.objects.all()[:5]
    return render(request, "index.html", context={"products": products_objs})


def products(request):
    products_objs = Product.objects.all()
    return render(request, "products.html", context={"products": products_objs})


def product(request, pk):
    product_obj = Product.objects.get(pk=pk)
    return render(request, "single-product.html", context={"product": product_obj})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def cart(request):
    products_objs = Product.objects.all()[:3]
    return render(request, "cart.html", context={"products": products_objs})
