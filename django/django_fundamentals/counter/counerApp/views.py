from operator import methodcaller
from urllib import request
from django.shortcuts import render, redirect

def counter(request):
    if 'count' not in request.session:
        request.session ['count'] = 0
    else:
        request.session ['count'] +=1
    return render(request, 'index.html')

def destroy(request):
    if request.method == 'post':
        del request.session['count']
    return redirect("/")

def add_tow(request):
    if request.method =='post':
        request.session['count']+=2
    return redirect("/")

