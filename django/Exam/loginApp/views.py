from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Plant, User
from django.contrib import messages
import bcrypt

def root(request):
    return render(request, "index.html")

def creat_user(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
        return redirect("/")
    else:
        pw_hash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            email = request.POST['email'],
            pw = pw_hash
        )
        request.session['user_id'] = new_user.id
        return redirect("/dashboard")

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
        return redirect("/")
    else:
        user=User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        request.session["firstname"] = user.fname
        request.session["lastname"] = user.lname
        return redirect("/dashboard")


def dashboard(request):
    if 'id' in request.session:
        context ={
            "this_user": User.objects.get(id = request.session['id']),
            "all_plants": Plant.objects.all(),
            "plants_planted_by_user":User.objects.get(id = request.session['id']).plants.all(),
            "plants_visited_by_user": User.objects.get(id =request.session['id']).visited_trees.all(),
        }
        return render(request, "homepage.html", context)
    else: 
        return redirect("/")

def new_tree(request):
    return render(request, "new_tree.html")

def add_new_tree(request):
    print("11111111111111111111111111111111")
    errors = Plant.objects.new_tree_validator(request.POST)
    print("hello")
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/new/tree') 
    else:
        Plant.objects.create(
        planted_by = User.objects.get(id = request.session["id"]),
        species = request.POST['species'],
        location = request.POST['location'],
        reason = request.POST['reason'],
        date = request.POST['date'],
        )
    return redirect("/dashboard")

def render_account(request):
    if 'id' in request.session:
        context ={
            "users": User.objects.all()
        }
        return render(request, "user_account.html", context)
    else: 
        return redirect("/")

def show_tree(request, tree_id):
    context = {
        "tree" : Plant.objects.get(id=tree_id),
    }
    return render(request, "show_tree.html", context)

def edit(request, tree_id):
    context={
        "the_tree": Plant.objects.get(id=tree_id)
    }
    return render(request, "editpage.html",context )


def delete(request, tree_id):
    tree = Plant.objects.get(id=tree_id)
    tree.delete()
    return redirect("/user/account")

def update(request, tree_id):
    errors=Plant.objects.new_tree_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/edit/' + str(tree_id)) 
    else:
        the_tree = Plant.objects.get(id=tree_id)
        the_tree.species = request.POST['species']
        the_tree.location = request.POST['location']
        the_tree.reason = request.POST['reason']
        the_tree.date = request.POST['date']
        the_tree.save()
        return redirect("/edit/"+ str(tree_id))
def destroy(request):
    del request.session['id']
    return redirect("/")
