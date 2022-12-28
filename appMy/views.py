from django.shortcuts import render, redirect
from .models import *


def index(request):
    
    context={}
    return render(request,'index.html',context)

def About(request):
    context={}
    return render(request,'about.html',context)

def Shop(request):
    product = Product.objects.all()

    context={
        "product":product,
    }
    return render(request,'shop.html',context)

def ShopSingle(request):
    context={}
    return render(request,'shop-single.html',context)

def Contact(request):
    context={}
    return render(request,'contact.html',context)

# Product
def createProduct(request):
    categorys = Category.objects.all()
    brands = Brand.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        price = request.POST["price"]
        image = request.FILES["image"]
        categoryid = request.POST["category"]
        categoryid = request.POST["brand"]
        category = categorys.get(id=categoryid)
        brand = brands.get(id=categoryid)

        product = Product(commentnum=0, stars=0, popular=0, category=category, brand=brand,
                          user=request.user, title=title, text=text, price=price, image=image)
        product.save()
        return redirect('index')
    context={
        "categorys":categorys,
        "brands": brands,
    }
    return render(request,"products/create.html", context)
