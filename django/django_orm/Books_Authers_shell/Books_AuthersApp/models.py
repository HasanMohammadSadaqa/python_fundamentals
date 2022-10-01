from email.policy import default
from enum import auto
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authers(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    notes = models.TextField(default="notes...")
    books = models.ManyToManyField(Books, related_name="authers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
