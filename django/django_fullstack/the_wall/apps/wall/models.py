import email
import imp
from unicodedata import name
from django.db import models
import re
import bcrybt 


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# name_regex = re.compile(r'^[a-zA-Z+$')
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors={}
        if len(postData['fname']) < 2:
            errors['fname']="First Name must be at least 2 charachters long."
        # if not name_regex.match(postData['fname']):
        #     errors['fname'] = "First name must include letters only"
        if len(postData['name']) < 2:
            errors['lname']="Last Name must be at least 2 charachters long."
        # if not name_regex.match(postData['lname']):
        #     errors['lname'] = "Last name must include letters only"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if len(postData['email']) < 1:
            errors['email']:"Email is required"
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 charachters."
        if postData['pw'] != postData['checkpw']:
            errors['checkpw'] = "Password do not match"
        return errors
    def login_validator(self,postData):
        errors={}
        checkemail=postData['email']
        user = User.objects.filter(email=checkemail)
        if len(user) < 1:
            errors['login']="Invalid email or password"
        elif not bcrybt.checkpw(postData['pw'].encode(), user[0].pw.encode()):
            errors['login']="Invalid email or password"
        return errors


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    user=models.ForeignKey(User, related_name="message")
    content=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


class Comment(models.Model):
    message=models.ForeignKey(Message, related_name="comment")
    user=models.ForeignKey(User, related_name="comment")
    content=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
