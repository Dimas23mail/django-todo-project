from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="todo_list/index.html")
