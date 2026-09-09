from django.shortcuts import render
from django.http import HttpResponse
from .models import Education

# Create your views here.

def about_page(request):
    return render(request, 'about/about.html')

def certificates_url(request):
    return HttpResponse("Welcome to the certificates page!")

def educaton_url(request):
    education_list = Education.objects.all().order_by('-graduation_date')

    context = {
        "education_list": education_list
    }

    return render(request, 'about/education.html', context)

def exp_page(request):
    return render(request, 'about/experience.html')