from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
def homepage(request):
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        uname=request.POST.get('firstname')
        ulast=request.POST.get('lastname')
        gender=request.POST.get('radio')

        if pass1!=pass2:
            return HttpResponse("your password and confirom are not the same")
        else:
            my_user=User.objects.create_user(email,pass1,uname)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("your Email id and password id wrong")

    return render(request, 'login.html')
