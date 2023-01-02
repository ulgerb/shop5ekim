from django.db import models
from django.contrib.auth.models import User



class Brand(models.Model):
    image = models.FileField(("Marka Logosu"), upload_to='', max_length=100, null=True)
    title = models.CharField(("Marka"), max_length=50)
    
    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    small = 'S'
    medium = 'M'
    large = 'L'
    xlarge = 'XL'
    xxlarge = 'XXL'
    Size = [
        (small, 'S'),
        (medium, 'M'),
        (large, 'L'),
        (xlarge, 'XL'),
        (xxlarge, 'XXL'),
    ]
    
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("Ürün Açıklaması"), max_length=500)
    image = models.FileField(("Ürün Resmi"), upload_to='', max_length=100)
    price = models.FloatField(("Fiyat"))
    stok = models.IntegerField(("Ürün Stok Sayısı"),null=True, default=1)
    size = models.CharField(max_length=4,choices=Size,default=medium,null=True)
    popular = models.IntegerField(("Popülerlik"))
    stars = models.FloatField(("Yıldız Ortalaması"))
    commentnum = models.IntegerField(("Yorum Sayısı"))
    
    def __str__(self):
        return self.title

class ShopBuy(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    adet = models.IntegerField(("Adet"))
    allprice = models.FloatField(("Toplam Fiyat"))
    size = models.CharField(("Beden"), max_length=50, null=True)
    
class Comment(models.Model):
    productid = models.ForeignKey(Product, verbose_name=("Yorum Yapılan Ürün"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("Yorum Yapan Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"))
    date_now = models.DateTimeField(("Paylaşma Tarihi"), auto_now_add=True)
    star = models.IntegerField(("Yıldız"))

    def __str__(self):
        return self.title
