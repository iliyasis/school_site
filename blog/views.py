from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from blog.models import *
# Create your views here.

def blog_list(request,author="None",cat="None"):
    if author != "None":
        posts = BlogPost.objects.filter(status=1,author__username=author)
        #context = {'posts': posts, 'author': author}
    elif cat != "None":
        posts = BlogPost.objects.filter(status=1,category__name=cat)
       # context = {'posts': posts, 'cat': cat}
    else:
        posts = BlogPost.objects.filter(status=1)
        #context = {'posts': posts, }

    if request.method == 'GET' and request.GET.get('s'):
        s = request.GET.get('s')
        posts = posts.filter(title__contains=s)

    posts = Paginator(posts, 3)
    page_number = request.GET.get("page")

    try:
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)#کار نمیکنه
    except EmptyPage:
        posts = posts.get_page(1)#کار نمیکنه


    context = {'posts': posts, 'cat': cat, 'author': author}


    return render(request, "blog/blog_list.html", context)

def blog_detail(request,slug):
    post = BlogPost.objects.get(slug=slug)
    context = {'post': post}
    return render(request, "blog/blog_detail.html", context)

def blog_manage(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, "blog/manage/admin-course-list.html",context)/