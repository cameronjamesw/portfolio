from django.contrib import admin
from .models import Project, Technology, Skill, Language

# Register your models here.

admin.site.register(Project)

admin.site.register(Technology)

admin.site.register(Language)

admin.site.register(Skill)
