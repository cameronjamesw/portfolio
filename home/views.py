from django.shortcuts import render
from django.http import HttpResponse

# Register your models here.

def index(request):
    return HttpResponse('Hello World!!')