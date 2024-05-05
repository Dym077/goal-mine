from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from manager.models import Goal, Task 
from .forms import TaskForm, GoalForm


# Create your views here.


class DeleteGoal(generic.ListView):
    
    def delete_goal(self, delete_goal_pk):
        goal_to_delete = get_object_or_404(Goal, pk=delete_goal_pk)
        goal_to_delete.delete()
        return redirect('home')

    
class EditGoal(generic.ListView):
    
    def edit_goal(request, edit_goal_pk):
        goal_to_edit = get_object_or_404(Goal, pk=edit_goal_pk)
        form = GoalForm(instance=goal_to_edit)
        list_of_goals = Goal.objects.all()
        return render(request, "todo/index.html", {"goals": list_of_goals, "form": form})
    
    def post(self, request, *args, **kwargs):
        edited_form = GoalForm(request.POST)
        print(edited_form)
        redirect('home')

class GoalsList(generic.ListView):
    
    def get(self, request, *args, **kwargs):
      
        goal_form = GoalForm()
        list_of_goals = Goal.objects.all()
        return render(request, "todo/index.html", {"goals": list_of_goals, "form": GoalForm})

    



    def post(self, request, *args, **kwargs):
        goal_form = GoalForm(request.POST)
        print(goal_form)
        if goal_form.is_valid():
            goal = goal_form.save(commit=False)
            goal.author = request.user
            goal.goal = goal
            print('VALID')
            goal.save()
        else:
            print('NOT VALID')
            goal_form = GoalForm()   
        return redirect('home')

        messages.add_message(
                    request, messages.SUCCESS, 'Your goal was successfully added'
                    )

        goal_form = GoalForm()          
        

    def goal_detail(request, pk):
        
        goal = get_object_or_404(Goal, pk=pk)
        tasks = goal.tasks.all().order_by("-created_on")
        task_count = len(tasks)
        task_form = TaskForm()
        goal_form = GoalForm()

        if request.method == "POST":
            
            task_form = TaskForm(data=request.POST)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.author = request.user
                task.goal = goal
                task.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Your task was successfully added'
                    )
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

        goal_form = GoalForm()        

        return HttpResponseRedirect(reverse('goal_detail', args=[slug]))      

        return render(
            request, "todo/index.html",
            {
                "goal": goal,
                "goals": goals,
                "goal_count": goal_count,
                "goal_form": goal_form

            },
        )  


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
