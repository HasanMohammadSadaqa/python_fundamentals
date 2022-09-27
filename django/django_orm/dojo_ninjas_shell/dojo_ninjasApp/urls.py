from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertion),
    path('add_dojo', views.dojo_creation),
    path('add_ninjas', views.ninjas_creation),
    
]