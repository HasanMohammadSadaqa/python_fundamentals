from django.shortcuts import render, redirect
from semi_restfulApp import models
from .models import Shows
from django.contrib import messages

def root(request):
    return redirect('/shows')


def show_all_shows(request):
    context={
        "all_shows": models.show_all_shows()
    }
    return render(request, "shows.html", context)

def new_show(request):
    return render(request, "new_show.html")

def adding_show(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/shows/new")
    created_show = models.create_show(request)
    return redirect(f"/shows/{created_show.id}")

def view_show(request, show_id):
    context={
        "the_show": Shows.objects.get(id=show_id)
    }
    return render(request, "view_show.html", context)

def delete_show(request, show_id):
    models.delete(request, show_id)
    return redirect('/')

def edit_show(request, show_id):
    context={
        "the_show":models.edit(request, show_id)
    }
    return render(request, "edit.html", context)

def updating_show(request, show_id):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect(f"/shows/{show_id}")
    models.update(request, show_id)
    return redirect('/shows/' + str(show_id))
    

