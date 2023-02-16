from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import *
from blog.urls import *
from blog.views import *

# Create your views here.

def home(request):
    allPost = Blog.objects.all()[0:1]
    params = {'allPost': allPost}
    return render(request, "home.html", params)

def about(request):
    allAbout = About.objects.all()
    params = {'allAbout': allAbout}
    # messages.success(request, "Welcome To iCoder About Us Page")
    return render(request, "about.html", params)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['desc']
        if name == "" or email == "" or phone == "" or msg == "":
            messages.warning(request, 'All Filed Are Requierd')
        else:
            contact = Contact(name=name, email=email,phone=phone,mess=msg)
            contact.save()
            messages.success(request, 'Contact is Suessfully is send')
    return render(request, "contact.html")

def handlesingup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['fisrtname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            return HttpResponse("Passwords do not match")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your Account To Created Succesfully is created in a Blog Website")
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        if loginusername == "admin" and loginpassword == "admin":
            allPost = Blog.objects.all()
            allCon = Contact.objects.all()
            params = {'allPost': allPost, 'allCon': allCon}
            messages.success(request, 'Suessfully User Logined')
            return render(request, "admin.html", params)

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Suessfully User Logined')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Username, Please Try Again')
            return redirect('/')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Succesfuly Logout in Blog Website')
    return redirect('/')

def handleblogs(request):
    allUser = User.objects.all()
    params = {"allUser": allUser}
    return render(request, "handleblogs.html", params)

# Not Found Page
def not_found(request, slug):
    params = {'slug': slug}
    return render(request, "notfound.html", params)