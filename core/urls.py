from django.urls import path 
from . import views

urlpatterns = [
    # This now handles http://djangoportfolionew-production.up.railway.app/
    path("", views.project_list, name="projects"), 
    
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
