from . import views
from django.urls import path

urlpatterns = [
    path('', views.GoalsList.as_view(), name='home'),
]