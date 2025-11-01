from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    # login
    path("login/", views.login_page, name="login"),
    # logout
    # path("logout/", views.logout, name="logout"),
    # sign_up
    path("siggn_up/", views.sign_up, name="sign_up"),
]