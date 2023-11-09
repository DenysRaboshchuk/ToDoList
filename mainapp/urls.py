from django.contrib import admin
from django.urls import path, include

from mainapp.views import (
    Index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    complete_or_not,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("task-add/", TaskCreateView.as_view(), name="task-add"),
    path("task-update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("complete-or-not/<int:pk>/", complete_or_not, name="complete-or-not"),

]

app_name = "mainapp"