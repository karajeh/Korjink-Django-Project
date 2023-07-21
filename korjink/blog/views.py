import imp
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Category
from .forms import CommentForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def RegisterPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        

    context = {'form' : form}
    return render (request,'blog/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'blog/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def the_dashboard(request):
    return render(request, 'blog/dashboard.html')

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status= Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status = Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status = Post.ACTIVE).filter( Q(title__icontains = query) | Q(intro__icontains = query) | Q(body__icontains = query))

    return render(request, 'blog/search.html', {'posts': posts, 'query' : query})