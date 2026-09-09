from django.urls import path
from . import views

urlpatterns = [
    path('certifications/', views.certificates_url, name="certifications"),
]
