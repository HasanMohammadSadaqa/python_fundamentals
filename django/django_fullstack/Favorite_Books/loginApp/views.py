from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

def root(request):
    return render(request, "index.html")

def creat_user(request):
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
        return redirect("/book")

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
        return redirect("/")
    else:
        user=User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        return redirect("/book")


def show_and_add(request):
    if 'id' in request.session:
        context ={
            "all_books":Book.objects.all(),
            "book_added_by_user":User.objects.get(id=request.session["id"]).books_uploaded.all(),
            "books_liked_by_user":User.objects.get(id =request.session['id']),
            "this_user": User.objects.get(id = request.session['id']).likes_books.all()
        }
        return render(request, "all_Books.html", context)
    else: 
        return redirect("/")

def add_book(request):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/book/")
    else:
        Book.objects.create(
            title = request.POST['title'],
            description = request.POST['desc'],
            uploaded_by = User.objects.get(id = request.session['id'])
        )
        return redirect("/book")

def destroy(request):
    del request.session['id']
    return redirect("/")
