from django.contrib import admin
from .models import Task
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)