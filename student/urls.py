from django.urls import path
from student import views

app_name = "news"

urlpatterns = [
    path("", views.dashboard,name="dashboard"),
]