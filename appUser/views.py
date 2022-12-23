from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


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
        # if len(password)>6:
        # else:
        #     return render(request, 'users/login.html', {"hata": "Şifrenin uzunluğu en az 6 olmalıdır"})
    context={
        
    }
    return render(request,'users/login.html',context)

def registerUser(request):
    
    return render(request,'users/register.html')