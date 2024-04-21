from django.shortcuts import render
from django.views import generic
from .models import Goal

# Create your views here.

class GoalsList(generic.ListView):
    queryset = Goal.objects.filter(status=1)
    template_name = "goal_list.html"