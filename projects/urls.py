from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list_url, name='projects'),
    path("<int:pk>/", views.project_detail_url, name="project_detail"),
]
