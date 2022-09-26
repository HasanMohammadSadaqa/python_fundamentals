from django.db import models


class Users(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Age = models.IntegerField()

# Create your models here.

def getusers():
    return Users.objects.all()


def create(request):
    Users.objects.create(
        Name=request.POST['first'],
        Email=request.POST['e-mail'],
        Age=request.POST['age'],
    )

# def delete():
#     c = Users.objects.all()
#     c.delete