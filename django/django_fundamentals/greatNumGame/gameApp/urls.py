from django.urls import path     
from . import views
urlpatterns = [
    path('', views.creat),
    path('putingNum', views.test),
    path('delete', views.play_again),
] 