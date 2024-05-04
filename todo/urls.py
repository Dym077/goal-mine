from . import views
from django.urls import path

urlpatterns = [
    path('', views.GoalsList.as_view(), name='home'),
   # path('todo/goal_detail.html', views.add_goal, name='add_goal'),   
    path('<int:pk>/', views.GoalsList.goal_detail, name='goal_detail'),
    path('delete/<int:delete_goal_pk>', views.DeleteGoal.delete_goal, name='goal_delete'),
    path('edit/<int:edit_goal_pk>', views.EditGoal.edit_goal, name='goal_edit'),
    
    path('<slug:slug>/edit_task/<int:task_id>', views.GoalsList.task_edit, name='task_edit'),
    path('<slug:slug>/delete_task/<int:task_id>', views.GoalsList.task_delete, name='task_delete'),
]
