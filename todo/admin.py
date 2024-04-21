from django.contrib import admin
from .models import Goal, Task
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Task)

@admin.register(Goal)
class GoalAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)