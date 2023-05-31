from django.urls import path
from todo import views

urlpatterns = [
    # Other URL patterns

    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
]
