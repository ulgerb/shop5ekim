"""shop5ekim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appMy.views import *
from appUser.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('hakkımızda/', About, name='About'),
    path('alışveriş/', Shop, name='Shop'),
    path('sepet/', shopBuy, name='shopBuy'),
    path('ürün/<id>/', ShopSingle, name='ShopSingle'),
    path('iletişim/', Contact, name='Contact'),
    # USER
    path('login/', loginUser, name='loginUser'), # giriş yap
    path('register/', registerUser, name='registerUser'), # kaydol
    path('logout/', logoutUser, name='logoutUser'),  # çıkış yap
    # PRODUCT
    path('create/', createProduct, name='createProduct'), # Ürün Oluştur
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
