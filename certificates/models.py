from django.db import models
from projects.models import Skill

# Create your models here.

class Certification(models.Model):

    name = models.CharField(max_length=100)

    provider = models.CharField(max_length=100)

    date_completed = models.DateField()

    expiry_date = models.DateField(
        blank=True,
        null=True
    )

    credential_url = models.URLField(
        blank=True
    )

    skills = models.ManyToManyField(
        Skill,
        blank=True
    )

    def __str__(self):
        return self.name
