from . import views
from django.urls import path

urlpatterns = [
    path('', views.GoalsList.as_view(), name='home'),
    path('<slug:slug>/', views.goal_detail, name='goal_detail'),
   
]