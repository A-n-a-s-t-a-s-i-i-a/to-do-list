from django import forms
from django.utils.timezone import localtime, now

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        widgets = {
            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'min': localtime(now()).strftime('%Y-%m-%dT%H:%M'),
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }
