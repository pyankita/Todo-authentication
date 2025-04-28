
from django.urls import path
from . import views

urlpatterns = [
    path("",views.TaskList.as_view(),name="task"),
    path("detail/<int:pk>/",views.TaskDetailView.as_view(),name="detail"),
    path("create/",views.TaskCreateView.as_view(),name="create"),
    path("update/<int:pk>/",views.TaskUpdateView.as_view(),name="update"),
    path("delete/<int:pk>/",views.TaskDeleteView.as_view(),name="delete")

]
