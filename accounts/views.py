from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect("index:home")
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {"form": form})
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"{username} .  ورود شما موفقیت آمیز بود ", "alert-success")
                return HttpResponseRedirect("/")
            else:
                print("Invalid username or password")
                messages.add_message(request, messages.ERROR, "ورود ناموفق!", "alert-danger")
                return HttpResponseRedirect("/accounts/login/")
        else:
            print("validation error")
            messages.add_message(request, messages.ERROR, "ورود ناموفق!", "alert-danger")
            return HttpResponseRedirect("/accounts/login/")

def sign_up(request):
     return render(request,"accounts/sign_up.html")