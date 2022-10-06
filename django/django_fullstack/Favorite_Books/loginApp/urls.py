from django.urls import path
from loginApp import views

urlpatterns = [
    path('', views.root),
    path('registration', views.creat_user),
    path('login', views.login),
    path('book/', views.show_and_add),
    path('add_favorite_book', views.add_book),
    path('destroy', views.destroy)
]