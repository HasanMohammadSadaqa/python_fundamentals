from django.urls import path
from wall import views


urlpatterns = [
    path('', views.root),
    path('registration', views.creat),
    path('login', views.login),
    path('show/', views.show),
    path('create/message', views.message),
    path('create/comment', views.comment),
    path('destroy', views.destroy)

]