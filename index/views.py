from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index/school-home.html")

def news(request):
    return render(request,"index/news-grid.html")

def blog(request):
    return render(request,"index/blog-grid.html")

def about(request):
    return render(request,"index/about.html")

def contact_us(request):
    return render(request,"index/contact-us.html")