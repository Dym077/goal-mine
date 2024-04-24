from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Goal

# Create your views here.

class GoalsList(generic.ListView):
    queryset = Goal.objects.filter(status=1)
    template_name = "todo/index.html"
    paginate_by = 6

def goal_detail(request, slug):
    queryset = Goal.objects.filter(status=1)
    goal = get_object_or_404(queryset, slug=slug)
    return render(request, "todo/goal_detail.html", {"goal": goal},) 

    


    