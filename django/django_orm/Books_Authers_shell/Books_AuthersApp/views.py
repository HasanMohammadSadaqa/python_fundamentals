from django.shortcuts import render, redirect,HttpResponse

def index(request):
    return HttpResponse("response from index method from root route, localhost:8000!")

# Create your views here.
