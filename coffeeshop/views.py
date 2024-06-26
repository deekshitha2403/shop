from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages

def create_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        discription = request.POST["discription"]
        price = request.POST["price"]
        image = request.FILES["image"]

        obj=Product(name=name,discription=discription, price=price, image=image, user=request.user)
        obj.save()
        messages.success(request," Product created successfully")
        return redirect("/")
    return render(request, "coffeeshop/create_product.html")

def product_list(request):
    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, "coffeeshop/product_list.html", context)    

def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, "coffeeshop/product_details.html", {'product' : product})


def product_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        discription = request.POST["discription"]
        price = request.POST["price"]
        image = request.FILES["image"]

        product.name = name
        product.discription = discription
        product.price = price
        product.image = image
        product.save()
        messages.success(request," Product updated successfully")
        return redirect("/")
    return render(request, "coffeeshop/product_update.html", {"products" : product})