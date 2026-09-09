from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_page, name="about"),
    path('certifications/', views.certificates_url, name="certifications"),
    path('education/', views.educaton_url, name="education"),
    path('experience/', views.exp_page, name="experience"),
]
