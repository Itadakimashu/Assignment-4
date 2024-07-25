from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForm
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs' : blogs})

def add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form' : form})


def delete(request, id):
    blog = Blog.objects.get(pk=id).delete()
    return redirect('home')

