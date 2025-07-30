from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.dashboard, name='dashboard'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.create_project, name='create_project'),
    path('tasks/<int:project_id>/', views.task_list, name='task_list'),
    path('tasks/add/<int:project_id>/', views.add_task, name='add_task'),
    path('tasks/comments/<int:task_id>/', views.task_comments, name='task_comments'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
