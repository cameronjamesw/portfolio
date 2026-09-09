from django.db import models
from projects.models import Skill, Technology
from django.core.exceptions import ValidationError
from django.utils import timezone

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


class Education(models.Model):
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    qualification = models.CharField(max_length=150)

    LEVEL_CHOICES = [
        ("bachelors degree", "Bachelor's Degree"),
        ("diploma", "Diploma"),
        ("certificate", "Certificate"),
        ("secondary", "Secondary Education"),
    ]

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        blank=True
    )

    start_date = models.DateField()
    graduation_date = models.DateField(
        blank=True,
        null=True
    )

    skills = models.ManyToManyField(Skill, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.qualification} - {self.institution}"

    def clean(self):
        if self.graduation_date:
            if self.graduation_date < self.start_date:
                raise ValidationError(
                    "Graduation date cannot be before the start date."
                )


class Experience(models.Model):
    job_role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)

    description = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)

    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True
    )

    skills = models.ManyToManyField("Skill", blank=True)
    technologies = models.ManyToManyField("Technology", blank=True)

    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.job_role} - {self.company_name}"

    def clean(self):
        if self.end_date:
            if self.end_date > timezone.now().date():
                raise ValidationError(
                    "End date cannot be in the future."
                )

            if self.end_date < self.start_date:
                raise ValidationError(
                    "End date cannot be before the start date."
                )

    @property
    def is_current(self):
        return self.end_date is None
