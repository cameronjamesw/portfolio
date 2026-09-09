from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about_page(request):
    return HttpResponse("About Page")

def certificates_url(request):
    return HttpResponse("Welcome to the certificates page!")

def educaton_url(request):
    return HttpResponse("Education Page")

def exp_page(request):
    return HttpResponse("Experience Page")