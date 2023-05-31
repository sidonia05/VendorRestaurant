from django.shortcuts import render, get_object_or_404
from django.views import View
from employee.models import Employee

class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employee/employee.html', {'employees': employees})

class EmployeeDetailsView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employee/employees-details.html', {'employee': employee})
