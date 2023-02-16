from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
# Class View
class GateWay():
    def __init__(self):
        print("hello")
# Create your views here.
def bloghome(request):
    allPost = Blog.objects.all()
    params = {'allPost': allPost}
    return render(request, "blog/bloghome.html", params)

def search(request):
    query = request.GET['search_her']
    allPost = Blog.objects.filter(title__icontains=query)
    params = {'allPost': allPost, 'query': query}
    return render(request, "blog/search.html", params)

def blogpost(request, slug):
    post = Blog.objects.filter(slug=slug).first()
    params = {'post':post}
    return render(request, "blog/blogpost.html", params)
