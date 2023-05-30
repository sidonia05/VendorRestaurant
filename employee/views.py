from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

from employee.models import Employee


class EmployeeView(View):
    def get(self, request):
        # Retrieve all employees from the database
        employees = Employee.objects.all()

        # Pass the employees to the template for rendering
        return render(request, 'employee/employee.html',
                      {'employees': employees})
