from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    # login
    path("login/", views.login_page, name="login"),
    # logout
    path("logout/", views.logout_page, name="logout"),
    # sign_up
    path("siggn_up/", views.signup_page, name="sign_up"),
]