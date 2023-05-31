from django.shortcuts import render, redirect
from .models import Employee, Todo

def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        employee_id = request.POST['employee_id']

        try:
            employee = Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            return redirect('employee_list')

        Todo.objects.create(title=title, description=description, employee=employee)
        return redirect('todo_list')
    else:
        employees = Employee.objects.all()
        return render(request, 'todo/create_todo.html', {'employees': employees})
