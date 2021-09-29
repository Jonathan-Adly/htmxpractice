from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/<int:task_id>/delete", views.delete, name="delete"),
    path("tasks/<int:task_id>/complete", views.complete, name="complete"),
]
