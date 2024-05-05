from django.shortcuts import render
from .models import Task

# Create your views here.

def task_manager(request):
    """
    Renders the Task page
    """
    manager = Task.objects.all().order_by('-updated_on').first()

    return render(request, "manager/task.html", {"manager": manager},)

    