from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json

def Home(request):
    return render(request, 'Home.html')


def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id=data['pid']
            # print(request.user.id)
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status': 'Product Already In Cart'}, status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status': 'Product Added To Cart'}, status=200)
                    else:
                        return JsonResponse({'status': 'Product Stack Not Avalabile'}, status=200)

            return JsonResponse({'status': 'Product Added To Cart Success'}, status=200)
        else:
            return JsonResponse({'status': 'Login To Add Cart'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=200)

# Login
def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login1')
    else:
        return render(request, 'login1.html')

# Registration
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email ID is already in use')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'User created successfully. Please login.')
                return redirect('Home')  # Redirect to the home page after successful registration
        else:
            messages.error(request, 'Passwords do not match')

    return redirect('login1')

def user_logout(request):
    logout(request)
    return redirect('Home')

def collections(request):
    categories = Catagory.objects.filter(status=0)
    return render(request, "petcollection.html", {"categories": categories})

def collectionsview(request, name):
    if (Catagory.objects.filter(name=name, status=0)):
        products = Product.objects.filter(catagory__name=name)
        return render(request, "indrx.html", {"products": products, "catagory_name": name})

def product_detail(request, cname, pname):
    catagory = Catagory.objects.filter(name=cname, status=0).first()
    if catagory:
        product = Product.objects.filter(name=pname, status=0).first()
        return render(request, "product_detail.html", {'product': product})
    else:
        messages.error(request, "no such product found")
        return redirect('collections')

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request, "cart.html", {"cart": cart})
    else:
        return redirect("/")

def remove_cart(request, cid):
    cartitem = Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")