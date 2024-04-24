from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200) 
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Task {self.body} | added by {self.author}"