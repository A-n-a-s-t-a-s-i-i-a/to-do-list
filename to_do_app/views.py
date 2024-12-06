from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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
    template_name = "to_do_app/delete.html"


def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = True
    task.save()
    return redirect("to_do_app:task_list")

def task_undo(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = False
    task.save()
    return redirect("to_do_app:task_list")


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "to_do_app/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    fields = ("name",)
    template_name = "to_do_app/tag_create.html"
    success_url = reverse_lazy("to_do_app:tags_list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("name",)
    template_name = "to_do_app/tag_create.html"
    success_url = reverse_lazy("to_do_app:tags_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "to_do_app/delete.html"
    success_url = reverse_lazy("to_do_app:tags_list")
