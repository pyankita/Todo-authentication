from django.urls import reverse_lazy
from .models import Task
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name="todo_app/login.html"
    fields="__all__"
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy("task")
    
class RegisterPage(FormView):
    template_name="todo_app/register.html"
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy("task")

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    template_name="todo_app/task_list.html"
    context_object_name="tasks"

    def get_context_data(self, **kwargs): # only user who have added task only one can see their tasks 
        context= super().get_context_data(**kwargs)
        context['tasks']=context["tasks"].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()  
        return context

class TaskDetailView(LoginRequiredMixin,DetailView):
    model=Task
    template_name="todo_app/task_detail.html"
    context_object_name="task"

class TaskCreateView(LoginRequiredMixin,CreateView):
    model=Task
    fields=["title","description","complete"] #display all field if only want one ==> ["title "]
    template_name="todo_app/task_create.html"
    success_url=reverse_lazy("task") #task is from the url redirect to the url 

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreateView,self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model=Task
    fields=["title","description","complete"] #display all field if only want one ==> ["title "]
    template_name="todo_app/task_create.html"
    success_url=reverse_lazy("task")

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name="tasks"
    success_url=reverse_lazy("task")
    template_name="todo_app/task_delete.html"

