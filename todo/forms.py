from manager.models import Task
from todo.models import Goal
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('body',)


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('body',)
