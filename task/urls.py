from django.urls import path
from task.views import TaskList, TaskDetail, TaskCreate, TaskDelete, TaskUpdate

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('tasks/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]

