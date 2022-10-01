from multiprocessing import context
from django.shortcuts import render, redirect
from Books_AuthersApp import models
from .models import Books, Authers


def show_books(request):
    context={
        "books" : models.show_books(),
    }
    return render(request, "books.html", context)

def add_book(request):
    models.adding_book(request)
    return redirect('/')

def view_of_book(request, book_id):
    context={
        "the_book": Books.objects.get(id = book_id),
        "the_auther": Authers.objects.all()
    }
    return render(request, "viewbook.html", context)

def adding_auther_to_book(request, book_id):
    models.add_auther_to_book(request, book_id)
    return redirect(f"/book/{book_id}")




def show_authers(request):
    context = {
        "authers" : models.show_authers(),
    }
    return render(request, "authers.html", context)

def add_auther(request):
    models.adding_auther(request)
    return redirect("/authers")

def view_of_auther(request, auther_id):
    context={
        "the_auther": Authers.objects.get(id = auther_id),
        "the_book" : Books.objects.all()
    }
    return render(request, "viewauther.html", context)

def adding_book_to_auther(request, auther_id):
    models.add_book_to_auther(request, auther_id)
    return redirect(f"/authers/{auther_id}")
