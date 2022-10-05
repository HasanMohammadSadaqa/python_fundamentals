from django.shortcuts import render, redirect
from log_regApp import models
from .models import User
from django.contrib import messages
import bcrypt

# def root(request):
#     return render(request, "log_reg.html")

def root(request):
    return render(request, "log_reg.html")

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
        password=pw_hash,
    )
    return redirect('/')


def check_login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user :
        loggd_user = user[0]
        if bcrypt.checkpw(request.POST['pass'].encode(), loggd_user.password.encode()):
            print('1')
            request.session['user_id'] = loggd_user.id
            request.session['name'] = loggd_user.first_name
            return redirect("/success")
        return redirect("/")

def show_registors(request):
    return render(request, 'welcoming.html')

def logout_user(request):
    del request.session["user_id"]
    del request.session["name"]
    return redirect("/")

