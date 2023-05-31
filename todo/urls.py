from django.urls import path
from todo import views

urlpatterns = [
    # Other URL patterns

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
]
