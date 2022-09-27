from multiprocessing import context
from pyexpat import model
from django.shortcuts import render, redirect
from dojo_ninjasApp import models


def insertion(request):
    context = {
        "Dojos" : models.insert(),
    }
    return render(request, "index.html", context)

def dojo_creation(request):
    models.create_dojo(request)
    return redirect("/")

def ninjas_creation(request):
    models.create_ninjas(request)
    return redirect("/")