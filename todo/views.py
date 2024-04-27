from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from manager.models import Goal, Task 
from .forms import TaskForm

# Create your views here.

class GoalsList(generic.ListView):
    queryset = Goal.objects.filter(status=1)
    template_name = "todo/index.html"
    paginate_by = 6

def goal_detail(request, slug):
    queryset = Goal.objects.filter(status=1)
    goal = get_object_or_404(queryset, slug=slug)
    tasks = goal.tasks.all().order_by("-created_on")
    task_count = len(tasks)

    if request.method == "POST":
        print("Received a TASK request")
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.author = request.user
            task.goal = goal
            task.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your task was successfully added'
                )

    task_form = TaskForm()
    print("About to render template")

    return render(request, "todo/goal_detail.html", {"goal": goal, "tasks": tasks, "task_count": task_count, "task_form": task_form,},) 

    
def task_edit(request, slug, task_id):
    """
    this view is for task editing
    """
    if request.method == "POST":

        queryset = Goal.objects.filter(status=1)
        goal = get_object_or_404(queryset, slug=slug)
        task = get_object_or_404(Task, pk=task_id)
        task_form = TaskForm(data=request.POST, instance=task)

        if task_form.is_valid() and task.author == request.user:
            task = task_form.save(commit=False)
            task.goal = goal
            task.appoved = False
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Task Updated')
        else:
            messages.add_messsage(request, message.ERROR, 'Error updating task')

    return HttpResponseRedirect(reverse('goal_detail', args=[slug]))        


def task_delete(request, slug, task_id):
    """
    In this view the delete task option is executed
    """
    queryset = Goal.objects.filter(status=1)
    goal = get_object_or_404(queryset, slug=slug)
    task = get_object_or_404(Task, pk=task_id)

    if task.author == request.user:
        task.delete()
        messages.add_message(request, messages.SUCCESS, 'Task was deleted')

    return HttpResponseRedirect(reverse('goal_detail', args=[slug]))    

    
        

    