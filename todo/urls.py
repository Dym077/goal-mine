from . import views
from django.urls import path

urlpatterns = [
    path('', views.GoalsList.as_view(), name='home'),
    path('todo/goal_detail.html', views.add_goal, name='add_goal'),   
    path('<slug:slug>/', views.goal_detail, name='goal_detail'),
    path('<slug:slug>/edit_task/<int:task_id>', views.task_edit, name='task_edit'),
    path('<slug:slug>/delete_task/<int:task_id>',
         views.task_delete, name='task_delete'),
      
   
]