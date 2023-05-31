from django.shortcuts import render, redirect
from django.views import View
from .models import Employee, Task

class TaskCreateView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'todo/create_task.html', {'employees': employees})

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        employee_id = request.POST['employee']
        employee = Employee.objects.get(id=employee_id)
        task = Task.objects.create(title=title, description=description, employee=employee)
        return redirect('task_list')

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'todo/task_list.html', {'tasks': tasks})
