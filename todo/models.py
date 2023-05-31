from django.db import models

from employee.models import Employee


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title