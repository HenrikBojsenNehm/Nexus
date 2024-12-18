from django.shortcuts import render

# Create your views here.
def store(req):
    context = {}
    return render(req, 'store/Store.html', context)

def cart(req):
    context = {}
    return render(req, 'store/Cart.html', context)

def checkout(req):
    context = {}
    return render(req, 'store/Checkout.html', context)