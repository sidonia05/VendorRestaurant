from django.http import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from task.forms import TaskForm
from task.models import Task


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


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_update.html'
    success_url = '/tasks/'


class TaskDelete(DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('task-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # Verifică dacă există o cerere de confirmare a ștergerii
        if 'confirm_delete' in request.POST:
            # Dacă da, șterge obiectul și redirecționează către succesul URL-ului
            return super().delete(request, *args, **kwargs)
        else:
            # Altfel, afișează un mesaj de confirmare
            context['confirm_message'] = 'Are you sure you want to delete this field?'

            return self.render_to_response(context)
