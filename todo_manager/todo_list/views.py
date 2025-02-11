from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ToDoItemCreateForm, ToDoItemUpdateForm
from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()
    return render(
        request=request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items}
    )


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[:2]


class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.filter(done=True).all()[:2]


class ToDoDetailView(DetailView):
    model = ToDoItem


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm
    #  fields = ("title", "description",)


class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = "_update_form"
    form_class = ToDoItemUpdateForm


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todo_list:list")
