from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Destination
from .models import Contact
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required



# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("register")
               
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"email already exists")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                user.save();
                return redirect("login")
           
        else:
            messages.info(request,"password not matching")
            return redirect("register")
           
    else:
        return render(request,'registration.html') 

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.warning(request,"invalid credentials")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("login")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def contact(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        feedback=request.POST['feedback']
        contact=Contact(firstname=firstname,lastname=lastname,email=email,feedback=feedback)
        contact.save()
    return render(request,"contact.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def about(request):
    return render(request,"about.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def shops(request):
    dests=Destination.objects.all()
    return render(request,"shops.html",{"dests":dests})

      


    