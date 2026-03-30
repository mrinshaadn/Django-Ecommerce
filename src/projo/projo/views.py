from django.shortcuts import render
from products.models import Product


def home(request):
    products = Product.objects.all().filter(is_active=True)
    # products = Product.objects.filter(is_available=True, is_featured=True)
    products = Product.objects.filter(is_active=True)[:8]
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request,'home.html',context)