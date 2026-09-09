from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about_page(request):
    return render(request, 'about/about.html')

def certificates_url(request):
    return HttpResponse("Welcome to the certificates page!")

def educaton_url(request):
    return render(request, 'about/education.html')

def exp_page(request):
    return render(request, 'about/experience.html')