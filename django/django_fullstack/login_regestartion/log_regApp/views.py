from multiprocessing import context
from django.shortcuts import render, redirect
from log_regApp import models
from .models import User
from django.contrib import messages
import bcrypt

# def root(request):
#     return render(request, "log_reg.html")

def root(request):
    context = {"users": User.objects.all()}
    return render(request, "log_reg.html", context)

def registration(request):
    errors = User.objects.validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    password = request.POST["pass"]
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    User.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        email=request.POST["email"],
        Password=pw_hash,
    )
    return redirect('/')


def check_login(request):
    user = User.objects.filter(email=request.POST["email"])
    if user:  # if True (email is found with registration database)
        logged_user = user[0]
        if bcrypt.checkpw(
            request.POST["password"].encode(), logged_user.password.encode()
        ):
            request.session["userid"] = logged_user.id
            return redirect(f"/success/{logged_user.id}")
        return redirect("/")

def show_registors(request,user_id):
    context={
        "user" : User.objects.get(id=user_id)
        }
    return render(request, 'welcoming.html', context)

def logout_user(request):
    del request.session["userid"]
    return redirect("/")

