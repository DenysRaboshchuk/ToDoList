from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from taskmanager.models import Task, Tag


class Index(generic.ListView):
    model = Task
    template_name = "taskmanager/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "taskmanager/task-form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("taskmanager:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "taskmanager/task-form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("taskmanager:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "taskmanager/confirm_delete.html"
    success_url = reverse_lazy("taskmanager:index")


def complete_or_not(request, pk):
    task = Task.objects.get(id=pk)
    task.task_done = not task.task_done
    task.save()
    return redirect("taskmanager:index")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "taskmanager/tag-list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    template_name = "taskmanager/tag-form.html"
    fields = "__all__"
    success_url = reverse_lazy("taskmanager:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    template_name = "taskmanager/tag-form.html"
    fields = "__all__"
    success_url = reverse_lazy("taskmanager:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "taskmanager/tag-confirm-delete.html"
    success_url = reverse_lazy("taskmanager:tags-list")
