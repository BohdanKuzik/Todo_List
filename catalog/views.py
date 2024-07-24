from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import TaskSearchForm, TaskForm
from catalog.models import Tag, Task


def home_redirect(request: HttpRequest) -> HttpResponseRedirect:
    return HttpResponseRedirect(reverse("catalog:task-list"))


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


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TagListView(generic.ListView):
    model = Tag
