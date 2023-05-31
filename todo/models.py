from django.db import models

from employee.models import Employee


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.title