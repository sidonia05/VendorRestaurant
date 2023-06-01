from django.views.generic import ListView, DetailView, CreateView
from task.forms import TaskForm
from task.models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/task_detail.html'

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_create.html'
    success_url = '/tasks/'




