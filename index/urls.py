from django.urls import path
from index import views

app_name = "index"

urlpatterns = [
    path("", views.home,name="home"),
    path("news/", views.news, name="news"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("contact_us/", views.contact_us, name="contact_us"),
]