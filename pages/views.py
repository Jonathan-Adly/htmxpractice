from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Task
from .forms import TaskForm


def home(request):
    tasks = Task.objects.all().order_by("pk")
    errors = None
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            errors = form.errors
        tasks = Task.objects.all()
        return render(
            request, "pages/tasks_list.html", {"tasks": tasks, "errors": errors}
        )
    return render(
        request, "pages/home.html", {"tasks": tasks, "form": form, "errors": errors}
    )


@require_http_methods(["DELETE"])
def delete(request, task_id):
    Task.objects.filter(id=task_id).delete()
    tasks = Task.objects.all().order_by("pk")
    return render(request, "pages/tasks_list.html", {"tasks": tasks})


@require_http_methods(["POST"])
def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.done == True:
        task.done = False
    else:
        task.done = True
    task.save()
    tasks = Task.objects.all().order_by("pk")
    return render(request, "pages/tasks_list.html", {"tasks": tasks})
