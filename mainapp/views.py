from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from mainapp.models import Task


class Index(generic.ListView):
    model = Task
    template_name = "mainapp/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "mainapp/task-form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("mainapp:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "mainapp/task-form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("mainapp:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "mainapp/confirm_delete.html"
    success_url = reverse_lazy("mainapp:index")


def complete_or_not(request, pk):
    task = Task.objects.get(id=pk)
    state = task.task_done
    if state:
        task.task_done = False
        task.save()
    else:
        task.task_done = True
        task.save()
    return redirect("mainapp:index")