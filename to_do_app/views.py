from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from to_do_app.models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "to_do_app/home.html"

