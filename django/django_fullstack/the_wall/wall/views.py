from multiprocessing import context
from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt


def root(request):
    return render(request, "index.html")

def creat(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
        return redirect("/")
    else:
        pw_hash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            email = request.POST['email'],
            pw = pw_hash
        )
        request.session['user_id'] = new_user.id
        return redirect("/show")

def login(request):
    errors = User.objects.login_validator(request.POST)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
            print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        return redirect("/")
    else:
        print("sssssssssssssssssssssssssssssssssssssss")
        user=User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        return redirect("/show")


def show(request):
    if 'id' in request.session:
        context ={
            "messages": Message.objects.all(),
            "comments": Comment.objects.all(),
            "this_user": User.objects.get(id = request.session['id'])
        }
        return render(request, "wall.html", context)
    else: 
        return redirect("/")


def message(request):
    Message.objects.create(
        user =User.objects.get(id=request.session['id']),
        content = request.POST['content']
    )
    return redirect("/show")


def comment(request):
    Comment.objects.create(
        message = Message.objects.get(id = request.POST['messageid']),
        user =User.objects.get(id=request.session['id']),
        content = request.POST['content']
    )
    return redirect("/show")  

def destroy(request):
    del request.session['id']
    return redirect("/")
