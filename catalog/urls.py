from django.urls import path

from catalog.views import (
    TagListView,
    TaskListView,
    TaskCreateView,
    home_redirect,
)

urlpatterns = [
    path("", home_redirect, name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "catalog"
