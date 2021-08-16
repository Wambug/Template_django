from django.urls import path
from .views import ProductDetailView,ProductView
from . import views 


urlpatterns = [
    path('',ProductView.as_view(),name="store"),
    path('product_detail/<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('cart',views.cart,name='cart'),
    path('add/',views.basket_add,name="basket_add"),
    path('delete/',views.basket_delete,name="basket_delete"),
    path('checkout',views.checkout,name='checkout'),
    path('products',views.products,name='products'),
    
]

