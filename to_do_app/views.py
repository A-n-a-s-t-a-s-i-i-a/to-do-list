from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from to_do_app.forms import TaskForm
from to_do_app.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "to_do_app/home.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_app/task_create.html"
    success_url = reverse_lazy("to_do_app:task_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_app/task_create.html"
    success_url = reverse_lazy("to_do_app:task_list")

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_app:task_list")
    template_name = "to_do_app/task_delete.html"


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "to_do_app/tag_list.html"
