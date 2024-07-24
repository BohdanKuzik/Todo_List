from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from catalog.forms import TaskSearchForm
from catalog.models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "catalog/task_list.html")


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("tags")
        params = self.request.GET.get("content")

        if params:
            queryset = queryset.filter(content__icontains=params)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        content = self.request.GET.get("content", "")
        context["form"] = TaskSearchForm(initial={"content": content})
        return context


class TagListView(generic.ListView):
    model = Tag
