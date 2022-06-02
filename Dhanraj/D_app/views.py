from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def buy(request):
    return render(request,'D_app/buy.html')

def sell(request):
    return render(request,'D_app/sell.html')

def donate(request):
    return render(request,'D_app/donate.html')
def index(request):
    return render(request,'D_app/index.html')


def home(request):
    return render(request,'D_app/home.html')

def sign_up(request):
    msg=''
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['psw1']
        pass2 = request.POST['psw2']
        if pass1 == pass2:
            try:
                u = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=pass1)
                u.save()
                alert='User Created Successfully !!..'
            except IntegrityError :
                msg='username alerady exist'
                return render(request,'D_app/sign_up.html',{'msg':msg})
            return redirect(reverse('D_app:log_in'))
        else:
            msg='Password does not match'
    return render(request,'D_app/sign_up.html',{'msg':msg})


def log_in(request):
    msg=''
    if request.method == 'POST':
        username = request.POST['uname']
        pass1= request.POST['psw']
        u = authenticate(username= username,password=pass1)
        if u is not None:
            login(request,user=u)
            return redirect(reverse('D_app:index'))
        else:
            msg='Invalid Details'
    return render(request,'D_app/log_in.html',{'msg':msg})

def log_out(request):
    logout(request)
    return redirect(reverse('D_app:home'))