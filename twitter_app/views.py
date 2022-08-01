from email.policy import default
from fileinput import filename
from os import name
from tkinter import ALL
from tkinter.ttk import Entry
from turtle import title
from django.shortcuts import render,redirect,reverse
from .models import Post,Favourite,Comment
from django.contrib.auth.models import User
from django.core.files.storage import  FileSystemStorage
from django.db.models import Q
from twitter_app.forms import RegisterForm




def index(request):
    post = Post.objects.all()
    return render(request,'twitter_app/index.html', {'post':post})

def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.author = User.objects.get(id=request.user.id)
        if request.FILES.get('image',False) !=False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            post.image = myfile
        post.save()
    return redirect('index')

def update(request,id):
    post = Post.objects.get (id = id) 
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        if request.FILES.get('image',False) !=False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            post.image = myfile
        post.author = User.objects.get(id=request.user.id)
        post.save()
        return redirect('index')
    return render(request, 'twitter_app/update.html', {'post':post})

def delete_post(request,id):
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('index'))
    return render(request, 'twitter_app/delete.html',{'post':post})

def search(request):
    quary = request.GET.get('search')
    search_obj = Post.objects.filter(Q(author=request.user))
    return render(request, 'twitter_app/search.html',{'quary':quary, 'search_obj':search_obj})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request,'twitter_app/register.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request,'twitter_app/registration/login.html', {'form':form})   

def regorlog(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request,'twitter_app/regorlog.html', {'form':form})   

def add_to_favourite(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.user.is_authenticated:
        if not request.user.favourite_set.filter(post=post).exists():
            item = Favourite()
            item.post = post
            item.user = request.user
            item.save()
        return redirect('index')
    return redirect('authorisation')

def delete_favourite(request, post_id):
    item = Favourite.objects.get(id = post_id)
    if request.user.is_authenticated:
        item.delete()
        return redirect('favourite')
    return redirect('authorisation')

def favourite(request):
    if request.user.is_authenticated:
        post = Favourite.objects.filter(user=request.user)
        return render(request, 'twitter_app/favourite.html', {'post':post})
    return redirect('authorisation')

def comment(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.comment_set.create(user = request.user,body=request.POST.get('body'))
        return redirect (reverse('post_detail', kwargs={'post_id':post.id}))
    return redirect (reverse('twitter_app/post_detail.html', kwargs={'post_id':post.id}))

def post_detail(request,post_id):
    post = Post.objects.get(id = post_id)
    return render(request,'twitter_app/post_detail.html',{'post': post})

