from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    start_date = models.DateField()
    completion_date = models.DateField(blank=True, null=True)

    technologies = models.ManyToManyField("Technology", blank=True)
    skills = models.ManyToManyField("Skill", blank=True)

    def __str__(self):
        return self.title


class Technology(models.Model):

    CATEGORY_CHOICES = [
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("database", "Database"),
        ("networking", "Networking"),
        ("tools", "Tools"),
    ]

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        blank=True
    )
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
