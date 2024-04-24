from . import views
from django.urls import path

urlpatterns = [
    path('', views.task_manager, name='manager'),
]