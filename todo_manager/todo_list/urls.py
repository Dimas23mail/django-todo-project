from django.urls import path

from . import views
from .views import ToDoListIndexView, ToDoListView, ToDoListDoneView, ToDoDetailView

app_name = 'todo_list'

urlpatterns = [
    #  path('', views.index_view, name="index"),
    #  path('', ToDoListIndexView.as_view(), name="index"),
    path('', ToDoListIndexView.as_view(), name="index"),
    path('<int:pk>', ToDoDetailView.as_view(), name="detail"),
    path('list/', ToDoListView.as_view(), name="list"),
    path('done/', ToDoListDoneView.as_view(), name="done"),

]
