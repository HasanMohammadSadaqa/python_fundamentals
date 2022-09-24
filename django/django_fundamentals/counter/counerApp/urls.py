from django.urls import path     
from . import views
urlpatterns = [
    path('', views.counter),
    path('destroy', views.destroy),
    path('add_two', views.add_tow),
]
