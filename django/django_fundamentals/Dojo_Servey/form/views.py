from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def creat_user(request):
    if request.method == "POST": 
        firstname_from_form = request.form["first_name"]
        lastname_from_form = request.form["last_name"]
        department_from_form = request.form["department"]
        username_from_form = request.form["user_name"]
        password_from_form = request.form['user_password']
        email_from_form = request.form["email"]
        number_from_form = request.form["contact_no"]
    return render(request, "show.html", first_name =firstname_from_form, last_name = lastname_from_form, department = department_from_form,
            username =username_from_form, password = password_from_form, email = email_from_form, num = number_from_form)

