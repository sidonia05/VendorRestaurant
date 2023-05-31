from django.urls import path

from todo import views

urlpatterns = [
    path('tasks/', views.create_todo, name = 'todo')

]
