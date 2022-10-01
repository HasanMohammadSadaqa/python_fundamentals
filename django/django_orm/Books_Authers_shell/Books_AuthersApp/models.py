from email.policy import default
from enum import auto
from importlib.metadata import requires
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authers(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    notes = models.TextField(default="")
    books = models.ManyToManyField(Books, related_name="authers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def show_books():
    return Books.objects.all()

def adding_book(request):
    Books.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )

# def view_book(request, book_id):
#     context={
#         "the_book": Books.objects.get(id = book_id),
#         "the_auther": Authers.objects.all()
#     }
#     return (request, context)

def add_auther_to_book(request, book_id):
    Books.objects.get(id = book_id).authers.add(Authers.objects.get(id=request.POST['select_auther']))



def show_authers():
    return Authers.objects.all()

def adding_auther(request):
    Authers.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )

def add_book_to_auther(request, auther_id):
        Authers.objects.get(id = auther_id).books.add(Books.objects.get(id=request.POST['select_book']))
