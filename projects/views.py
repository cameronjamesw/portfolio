from django.shortcuts import render
from .models import Project, Language, Technology

# Create your views here.

def project_list_url(request):
    technologies = Technology.objects.all().order_by('category', 'name')
    languages = Language.objects.all()

    selected_technology = request.GET.get('technology')
    selected_language = request.GET.get('language')

    project_list = Project.objects.all().prefetch_related('technologies', 'skills').order_by('-start_date')

    if selected_technology:
        projects = projects.filter(technologies__id=selected_technology)

    if selected_language:
        projects = projects.filter(languages__id=selected_language)

    return render(request, 'projects/projects.html', {
        'project_list': project_list,
        'technologies': technologies,
        'languages': languages,
        'selected_technology': selected_technology,
        'selected_language': selected_language,
    })
