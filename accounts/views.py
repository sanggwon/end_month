from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Follower, Following
# Create your views here.

def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect("posts:list")
    else :
        login_form = AuthenticationForm(request)
    return render(request,"accounts/login.html", {"login_form":login_form})

def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("accounts:login")
    else:
        user_form = UserCreationForm()
    return render(request,"accounts/signup.html",{"user_form":user_form})
 
@login_required  
def logout(request):
    auth_logout(request)
    return redirect("accounts:login")
    
def list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, "accounts/list.html",{"users":users})
    
def detail(request,id):
    User = get_user_model()
    user = User.objects.get(id=id)
    return render(request, "accounts/detail.html",{"user":user})
    
def follow(request,id):
    User = get_user_model()
    me = request.user
    you = User.objects.get(id=id)
    
    if me != you :
        for m in me.link_set.all():

    return redirect('accounts:user_page', id)
    
    