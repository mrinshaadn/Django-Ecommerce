from django.urls import path,include
from .views import product_detail,store,search
urlpatterns = [
    # path('', home, name = 'home'),
    path('', store, name = 'store'),
    path('category/<slug:category_slug>/', store,name='products_by_category'),
    path('category/<slug:category_slug>/<slug:products_slug>/', product_detail,name='product_detail'),
    path('search/',search , name ='search')
]