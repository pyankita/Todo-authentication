from django.urls import reverse_lazy
from .models import Task
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView


class TaskList(ListView):
    model=Task
    template_name="todo_app/task_list.html"
    context_object_name="tasks"

class TaskDetailView(DetailView):
    model=Task
    template_name="todo_app/task_detail.html"
    context_object_name="task"

class TaskCreateView(CreateView):
    model=Task
    fields="__all__" #display all field if only want one ==> ["title "]
    template_name="todo_app/task_create.html"
    success_url=reverse_lazy("task") #task is from the url redirect to the url 

class TaskUpdateView(UpdateView):
    model=Task
    fields="__all__" #display all field if only want one ==> ["title "]
    template_name="todo_app/task_create.html"
    success_url=reverse_lazy("task")

class TaskDeleteView(DeleteView):
    model=Task
    context_object_name="tasks"
    success_url="task"
    template_name="todo_app/task_delete.html"
