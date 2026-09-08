from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def project_url(index):
    return HttpResponse('This is the projects URL!!')
