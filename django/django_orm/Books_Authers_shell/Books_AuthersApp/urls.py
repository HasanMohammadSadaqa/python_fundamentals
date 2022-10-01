from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_books),
    path('Add_books', views.add_book),
    path('book/<int:book_id>/', views.view_of_book),
    path('adding_authers_to_book/<int:book_id>/', views.adding_auther_to_book),
    path('authers/', views.show_authers),
    path('authers/Add_authers', views.add_auther),
    path('authers/<int:auther_id>/', views.view_of_auther),
    path('adding_books_to_auther/<int:auther_id>/', views.adding_book_to_auther),
    # path('', views.show_authers),
    # path('Add_authers', views.add_auther),
]
