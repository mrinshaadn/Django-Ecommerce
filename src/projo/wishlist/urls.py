from django.urls import path
from . import views

urlpatterns = [
    # ... existing urls ...
    path('wishlist/', views.wishlist_page, name='wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
]