from django.contrib import admin
from .models import Goal
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Goal)
class GoalAdmin(SummernoteModelAdmin):    


    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)



