# core/urls.py
from django.urls import path 
from . import views

urlpatterns = [
    path("", views.project_list, name="projects"),         # Works at /
    path("projects/", views.project_list, name="projects_list"), # Works at /projects/
    
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
