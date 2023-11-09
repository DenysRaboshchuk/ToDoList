from django.shortcuts import render

from mainapp.models import Task


# Create your views here.
def index(request):
    context = {
        "tasks": Task.objects.all()
    }
    return  render(request, "mainapp/index.html", context=context)