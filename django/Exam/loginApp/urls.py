from django.urls import path
from loginApp import views

urlpatterns = [
    path('', views.root),
    path('registration', views.creat_user),
    path('login', views.login),
    path('dashboard/', views.dashboard),
    path('new/tree', views.new_tree),
    path('add_new_tree', views.add_new_tree),
    path('user/account', views.render_account),
    path('show/<int:tree_id>', views.show_tree),
    path('edit/<int:tree_id>/', views.edit),
    path('delete/<int:tree_id>/', views.delete),
    path('update/<int:tree_id>', views.update),
    path('destroy', views.destroy)
]