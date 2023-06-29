from django.contrib import admin
from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    search_fields = ('task',)



admin.site.register(Task, TaskAdmin)
