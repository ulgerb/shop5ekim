from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Giriş Yap
def loginUser(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request, 'users/login.html', {"hata":"Kullanıcı adı veya şifre yanlış!"})
        
    context={
        
    }
    return render(request,'users/login.html',context)

# Kaydol
def registerUser(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 == password2:
            if len(password1) >= 6:
                boolup = False
                boolnum = False
                for harf in password1:
                    if harf.isupper():
                        boolup = True
                    if harf.isnumeric():
                        boolnum = True
                if boolup and boolnum:
                    if not User.objects.filter(username=username).exists():
                        if not User.objects.filter(email=email).exists():
                            user = User.objects.create_user(username=username, password=password1, email=email, first_name=name, last_name=surname)
                            user.save()
                            return redirect('loginUser')
                        else:
                            return render(request, 'users/register.html', {"hata": "Bu email zaten kullanılıyor!"})
                    else:
                        return render(request, 'users/register.html', {"hata": "Bu kullanıcı adı zaten kullanılıyor!"})
                else:
                    return render(request, 'users/register.html', {"hata": "Şifre sayı içermeli ve bir harfi büyük olmalıdır!"})
            else:
                return render(request, 'users/register.html', {"hata": "Şifrenin uzunluğu en az 6 olmalıdır"})
        else:
            return render(request, 'users/register.html', {"hata": "Şifreler aynı değil!"})
                
    return render(request,'users/register.html')

# Çıkış Yap
def logoutUser(request):
    logout(request)
    return redirect('index')

