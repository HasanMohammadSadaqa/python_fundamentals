from turtle import title
from urllib import request
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField()
# ninjas = []

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

def insert():
    return Dojo.objects.all()

def create_dojo(request):
    # if request.POST['add_dojo'] == "Add":
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )

def create_ninjas(request):
    # if request.POST['add_ninjas'] == "Add":
    Ninja.objects.create(
        dojo = Dojo.objects.get(id = int(request.POST['dojo'])),
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )