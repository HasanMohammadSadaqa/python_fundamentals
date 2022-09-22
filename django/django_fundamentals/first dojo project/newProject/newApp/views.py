from contextlib import redirect_stderr
from django.shortcuts import render,redirect, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("blogs/")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def creat(request):
    return redirect("/")

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request):
    return redirect("blogs/")

def bonus(request):
    return JsonResponse({"title" : "My first blog", "content":"Lorem, ipsum dolar sit amet consectetur adipisicing elite." })

