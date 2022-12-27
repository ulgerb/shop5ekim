from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("Ürün Açıklaması"), max_length=500)
    image = models.FileField(("Ürün Resmi"), upload_to='', max_length=100)
    price = models.FloatField(("Fiyat"))
    popular = models.IntegerField(("Popülerlik"))
    stars = models.FloatField(("Yıldız Ortalaması"))
    commentnum = models.IntegerField(("Yorum Sayısı"))
    
class Comment(models.Model):
    productid = models.ForeignKey(Product, verbose_name=("Yorum Yapılan Ürün"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("Yorum Yapan Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"))
    date_now = models.DateTimeField(("Paylaşma Tarihi"), auto_now_add=True)
    star = models.IntegerField(("Yıldız"))