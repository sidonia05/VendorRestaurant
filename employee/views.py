from django.shortcuts import render
from django.views import View
from employee.models import Employee

class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employee/employee.html', {'employees': employees})
