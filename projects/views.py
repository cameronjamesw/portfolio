from django.shortcuts import render
from .models import Project, Technology

# Create your views here.

def project_list_url(request):
    technology_id = request.GET.get('technology')

    project_list = Project.objects.all().prefetch_related('technologies', 'skills').order_by('-start_date')

    if technology_id:
        project_list = project_list.filter(technologies__id=technology_id)

    technologies = Technology.objects.all().order_by('category', 'name')

    return render(request, 'projects/projects.html', {
        'project_list': project_list,
        'technologies': technologies,
        'selected_technology': technology_id,
    })
