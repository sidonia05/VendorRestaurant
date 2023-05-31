from django.shortcuts import render

def task_list(request):
    tasks = []  # Replace this with your logic to fetch the list of tasks
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        # Handle form submission and task creation here
        pass
    else:
        return render(request, 'todo/task_create.html')

