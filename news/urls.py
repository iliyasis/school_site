from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    path("", views.news_list,name="news_list"),
    path("detail/", views.news_detail,name="news_detail"),
]