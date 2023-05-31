from django.urls import path
from employee.views import EmployeeView, EmployeeDetailsView

urlpatterns = [
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('employee/details/<int:pk>/', EmployeeDetailsView.as_view(), name='employee_details'),
]
