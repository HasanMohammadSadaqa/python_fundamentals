from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('reg/', views.registration),
    path("login/", views.check_login),
    path("success/<int:user_id>", views.show_registors),
    path("logout/", views.logout_user),
]
