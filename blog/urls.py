from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_list,name="blog_list"),
    path("detail/<slug>", views.blog_detail,name="blog_detail"),
    path("manage/", views.blog_manage,name="blog_manage"),
]