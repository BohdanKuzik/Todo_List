from django.urls import path

from catalog.views import (
    TagListView,
    TaskListView,
    TaskCreateView,
    home_redirect,
    toggle_complete_todo,
    TaskDeleteView,
    TaskUpdateView,
)

urlpatterns = [
    path(
        "",
        home_redirect,
        name="home"
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/create",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tasks/<int:pk>/toggle-complete/",
        toggle_complete_todo,
        name="toggle-complete"
    ),
]

app_name = "catalog"
