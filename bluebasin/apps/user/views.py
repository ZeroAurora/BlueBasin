from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import auth

from .forms import InfoSettingsForm, PasswordSettingsForm, LoginForm, SignupForm
from .models import User

from bluebasin.apps.identity.models import Identity

# todo: use template to render errors.

def settings(request):
    return render(request, "user/settings.html")


def settings_info(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    form = InfoSettingsForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        user = request.user
        user.email = email
        user.phone = phone
        user.save()
    else:
        return HttpResponse("Invalid form data")
    return render(request, "user/settings_info.html")


def settings_password(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    form = PasswordSettingsForm(request.POST)
    if form.is_valid():
        old_password = form.cleaned_data["old_password"]
        new_password = form.cleaned_data["new_password"]
        confirm_password = form.cleaned_data["confirm_password"]
        if new_password != confirm_password:
            return HttpResponse("Passwords do not match")
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
        else:
            return HttpResponse("Invalid password")
    return render(request, "user/settings_password.html")


def signup(request: HttpRequest):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if password != confirm_password:
                return HttpResponse("Password and confirm password do not match")
            user = auth.authenticate(request, username=username, password=password)
            if user:
                return HttpResponse("User already exists")
            else:
                user = User.objects.create_user(
                    username=username, email=email, phone=phone, password=password
                )
                user.save()
                return redirect("user_login")
    return render(request, "user/signup.html")


def login(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                if iden := Identity.objects.filter(user=user).first():
                    request.session["identity"] = iden.pk
                    return redirect("index")
                else:
                    iden = Identity.objects.create(user=user)
                    request.session["identity"] = iden.pk
                    return redirect("welcome")
            else:
                return HttpResponse("Invalid username or password")
    return render(request, "user/login.html")


def logout(request: HttpRequest):
    if request.method == "POST":
        auth.logout(request)
    return redirect("index")


def reset_password(request: HttpRequest):
    return render(request, "user/reset_password.html")
