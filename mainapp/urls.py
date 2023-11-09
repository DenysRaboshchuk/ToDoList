from django.contrib import admin
from django.urls import path, include

from mainapp.views import (
    Index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    complete_or_not,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("task-add/", TaskCreateView.as_view(), name="task-add"),
    path("task-update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("complete-or-not/<int:pk>/", complete_or_not, name="complete-or-not"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>/", TagsDeleteView.as_view(), name="tags-delete"),

]

app_name = "mainapp"