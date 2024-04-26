from django.db import models
from django.contrib.auth.models import User
from todo.models import Goal

# Create your models here.

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Task {self.body} | added by {self.author}"    

