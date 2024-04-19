from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_todo(request):
    return HttpResponse("My to do list")