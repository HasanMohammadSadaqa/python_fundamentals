
from django.db import models
import re


class UserManager(models.Manager):
    def validation(self, postdata):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):                
            errors['email'] = "Invalid email address!"
        if len(postdata["first_name"]) < 2 :
            errors["first_name"] = "first name shouldn't be less than 2 charachters"
        if len(postdata['last_name']) < 2 :
            errors['last_name'] = "last name shouldn't be less than 2 charachters"
        if len(postdata["pass"]) < 8:
            errors["password"] = "Password should be 8 characters minimum"
        if postdata["pass"] != postdata["passconf"] and postdata["passconf"] != 0:
            errors["check"] = "Password should match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()


