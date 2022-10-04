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
    user = User.objects.filter(email=request.POST['email'])
    if user :
        loggd_user = user[0]
        if bcrypt.checkpw(request.POST['pass'].encode(), loggd_user.Password.encode()):
            print('1')
            request.session['user_id'] = loggd_user.id
            request.session['name'] = loggd_user.first_name
            return redirect("/success")
        return redirect("/")





    # user = User.objects.filter(email=request.POST["email"])
    # print("1")
    # if user:  # if True (email is found with registration database)
    #     print("2")
    #     logged_user = user[0]
    #     print("3")
    #     # if bcrypt.checkpw(request.POST['pass'].encode(), logged_user.Password.encode()):
    #     if bcrypt.checkpw(request.POST['pass'].encode(), logged_user.Password.encode()):
            
    #             print("4")
    #             request.session["userid"] = logged_user.id
    #             request.session['name'] = logged_user.first_name
    #             print("5")
    #             return redirect("/success")
    #     return redirect("/")

def show_registors(request):
    return render(request, 'welcoming.html')

def logout_user(request):
    del request.session["userid"]
    del request.session["name"]
    return redirect("/")

