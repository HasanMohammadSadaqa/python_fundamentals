from multiprocessing import context
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def creat_user(request):
    if request.method == "POST": 
        firstname_from_form = request.POST["first_name"]
        lastname_from_form = request.POST["last_name"]
        department_from_form = request.POST["department"]
        username_from_form = request.POST["user_name"]
        password_from_form = request.POST['user_password']
        email_from_form = request.POST["email"]
        number_from_form = request.POST["contact_no"]
        context = {
            "first_name" : firstname_from_form,
            "last_name" : lastname_from_form,
            "department" : department_from_form,
            "username" : username_from_form,
            "password" :  password_from_form, 
            "email" : email_from_form,
            "num" : number_from_form
        }
    return render(request, "show.html", context)
    

