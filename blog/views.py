from django.shortcuts import render
from blog.models import *
# Create your views here.

def blog_list(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, "blog/blog_list.html", context)

def blog_detail(request,slug):
    post = BlogPost.objects.get(slug=slug)
    context = {'post': post}
    return render(request, "blog/blog_detail.html", context)