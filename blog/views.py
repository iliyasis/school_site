from django.shortcuts import render
from blog.models import *
# Create your views here.

def blog_list(request,author=None,cat=None):
    if author:
        posts = BlogPost.objects.filter(status=1,author__username=author)
        context = {'posts': posts, 'author': author}
    elif cat:
        posts = BlogPost.objects.filter(status=1,category__name=cat)
        context = {'posts': posts, 'cat': cat}
    elif request.method == 'GET' and request.GET.get('s'):
        s = request.GET.get('s')
        posts = BlogPost.objects.filter(title__contains=s)
        context = {'posts': posts}
    else:
        posts = BlogPost.objects.filter(status=1)
        context = {'posts': posts, }


    return render(request, "blog/blog_list.html", context)

def blog_detail(request,slug):
    post = BlogPost.objects.get(slug=slug)
    context = {'post': post}
    return render(request, "blog/blog_detail.html", context)

def blog_manage(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, "blog/manage/admin-course-list.html",context)