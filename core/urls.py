from django.urls import path 
from . import views

urlpatterns = [
    path("projects/", views.project_list, name="projects"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]