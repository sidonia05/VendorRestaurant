from django.db import models
from employee.models import Employee

class Task(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(max_length=50)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.title}'

    class Meta:
        ordering = ['complete']


