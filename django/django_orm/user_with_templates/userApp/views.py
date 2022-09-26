from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Users
from userApp import models

def index(request):
    context = {
        "users" : models.getusers(),
    }
    return render(request, "index.html", context)

def createuser(request):
    models.create(request)
    return redirect("/")

# def delete():
#     models.delete()
#     return redirect("/")




