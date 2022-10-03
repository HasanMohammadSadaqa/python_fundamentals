from django.urls import path
from . import views

urlpatterns = {
    # path('', views.root),
    path('', views.show_all_shows),
    path('shows/new/', views.new_show),
    path('shows/create/', views.adding_show),
    path('shows/<int:show_id>/', views.view_show),
    path('shows/<int:show_id>/edit/', views.edit_show),
    path('shows/<int:show_id>/update', views.updating_show),
    path('shows/<int:show_id>/destroy', views.delete_show),
    path('go back', views.Go_back),


}