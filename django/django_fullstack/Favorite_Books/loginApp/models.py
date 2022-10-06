from django.db import models
import re
import bcrypt 


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# name_regex = re.compile(r'^[a-zA-Z+$')
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors={}
        if len(postData['fname']) < 2:
            errors['fname']="First Name must be at least 2 charachters long."
        # if not name_regex.match(postData['fname']):
        #     errors['fname'] = "First name must include letters only"
        if len(postData['lname']) < 2:
            errors['lname']="Last Name must be at least 2 charachters long."
        # if not name_regex.match(postData['lname']):
        #     errors['lname'] = "Last name must include letters only"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if len(postData['email']) < 1:
            errors['email'] = "Email is required"
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 charachters."
        if postData['pw'] != postData['checkpw']:
            errors['checkpw'] = "Password do not match"
        return errors

    def login_validator(self,postData):
        errors={}        
        checkemail=postData['email']
        if checkemail=='':
            errors['email_empty']="Email is empty"
            return errors
        user = User.objects.filter(email=checkemail)
        if not user:
            errors['wrong_email']="Email is not found"
            return errors
        if not bcrypt.checkpw(postData['pw'].encode(), user[0].pw.encode()):
            errors['password']="Invalid password"
        return errors 


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data["title"]) < 1:
            errors["title"] = "Title can't be empty!"
        if len(data["desc"]) < 5:
            errors["description"] = "Description has to be minimum 5 characters"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    #the user who uploaded a certain book
    users_who_like = models.ManyToManyField(User, related_name="likes_books")
    #list of users who like a certain book
    objects = BookManager()
