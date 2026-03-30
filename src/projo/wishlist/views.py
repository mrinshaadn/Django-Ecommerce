from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Wishlist
from products.models import Product


@login_required
def toggle_wishlist(request, product_id):
    """
    AJAX call — product wishlist-ൽ add/remove ചെയ്യുന്നു.
    Returns JSON: { "status": "added" | "removed", "count": int }
    """
    product = get_object_or_404(Product, id=product_id)
    obj, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if not created:
        obj.delete()
        status = "removed"
    else:
        status = "added"

    count = Wishlist.objects.filter(user=request.user).count()
    return JsonResponse({"status": status, "count": count})


@login_required
def wishlist_page(request):
    """Wishlist page — user-ന്റെ saved products കാണിക്കുന്നു."""
    items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist.html', {'items': items})