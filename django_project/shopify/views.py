from django.http.response import JsonResponse
from shopify.basket import Basket
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView,ListView
from .models import Product

# Create your views here.
class ProductView(ListView):
    model = Product
    template_name = 'shopify/store.html'
    context_object_name = 'products'


def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'shopify/products.html',context)

class ProductDetailView(DetailView):
    model = Product

def basket_add(request):
    basket = Basket(request)
    print(request.POST)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productdty'))
        product = get_object_or_404(Product,id=product_id)
        basket.add(product=product,qty=product_qty)
        basketqty = basket.__len__() 
        response = JsonResponse({'qty':basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        print(product_id)
        basket.delete(product=product_id)
        response = JsonResponse({'Success':True})
        return response

def cart(request):
    basket = Basket(request)
    print(basket)
    return render(request,'shopify/cart.html',{'basket':basket})



def checkout(request):
    context = {}

    return render(request,'shopify/checkout.html',context)
