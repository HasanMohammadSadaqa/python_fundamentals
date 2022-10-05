from django.urls import path
from loginApp import views

urlpatterns = [
    path('', views.root),
    path('registration', views.creat),
    path('login', views.login),
    path('show/', views.show),
    path('destroy', views.destroy)
]