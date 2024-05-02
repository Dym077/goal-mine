from django.db import models
from django.contrib.auth.models import User
from todo.models import Goal

# Create your models here.

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="tasks") 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Task {self.body} | added by {self.author}"    

    def profile_page(request):
        user = get_object_or_404(User, user=request.user)
        tasks = user.author.all()    

