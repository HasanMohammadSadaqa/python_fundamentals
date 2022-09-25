from django.shortcuts import render, redirect
import random

def creat(request):
    if 'target' not in request.session :
        request.session['target'] = random.randint(1,100)
    return render(request, "index.html")

def test(request):
    if request.method == "POST":
        if int(request.POST['guess']) == request.session['target'] :
            request.session['result'] = "correct"
        elif int(request.POST['guess']) > request.session['target']:
            request.session['result'] = "high"
        else:
            request.session['result'] = "low"
        return redirect("/")
def play_again(request):
    del request.session['target']
    return redirect("/")

# Create your views here.
