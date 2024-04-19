from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_todo(request):
    return HttpResponse("My to do list")