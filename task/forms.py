from django import forms
from task.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.Textarea(attrs={'rows': 3}),
        }
