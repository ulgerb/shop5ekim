from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *


def index(request):
    
    context={}
    return render(request,'index.html',context)

def About(request):
    context={}
    return render(request,'about.html',context)

    
# Product
def Shop(request):
    product = Product.objects.all()

    context={
        "product":product,
    }
    return render(request,'shop.html',context)

def ShopSingle(request,id):
    product = get_object_or_404(Product, id=id)
    comments = Comment.objects.filter(productid=id) # ürüne yapılan yorumlar
    sumstar = 0
    
    if request.method == "POST":
        size = request.POST['size']
        updateproduct = ShopBuy.objects.filter(user=request.user, product=product, size = size)
        adet = request.POST['adet']
        fiyat = product.price * int(adet)
        
        if updateproduct.exists():
            updateproduct.update(adet=adet)
            updateproduct.update(allprice=fiyat)
            
        else:
            shopbuy = ShopBuy(adet=adet, allprice=fiyat, size=size,product=product, user=request.user)
            shopbuy.save()
            
        return HttpResponseRedirect('/ürün/'+id+'/')
    
    if request.method == "POST":
        try:
            title = request.POST["title"]
            text = request.POST["text"]
            star = request.POST["star"]
            # ürüne yapılan yorumları çek, star sayılarını topla ve toplam yoruma böl
            comment = Comment(productid=product,user=request.user,title=title,text=text,star=star)
            comment.save()
            product.commentnum = len(list(comments))
            
            for i in comments:
                sumstar += i.star
            stars = sumstar/len(list(comments))
            
            product.stars = stars
            product.save()
            return HttpResponseRedirect('/ürün/'+id+'/')
        except:
            pass
        
        
    
    context = {
        "product": product,
        "comments": comments,
    }
    return render(request, 'shop-single.html', context)


def shopBuy(request):
    shoping = ShopBuy.objects.filter(user=request.user)
    
    if request.method == "POST":
        key = list(request.POST)[1]
        values = request.POST[key]
        productid = key[4:]
        product = shoping.get(id=productid)
        product.adet = values
        product.allprice = int(values) * product.product.price
        product.save()
        return redirect('shopBuy')        
        
    context = {
        'shoping': shoping,
    }
    return render(request, 'shop-buy.html', context)

# Ürün Oluştur
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


def Contact(request):
    context={}
    return render(request,'contact.html',context)