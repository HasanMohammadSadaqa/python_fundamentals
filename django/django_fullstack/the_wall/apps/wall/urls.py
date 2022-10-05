from django.urls import path

from apps.wall import views
from . import urls

urlspatterns = [
    path('', views.root),
    path('registration', views.creat),
    path('login', views.login),
    path('show/', views.show),
    path('create/message', views.message),
    path('create/comment', views.comment)

]