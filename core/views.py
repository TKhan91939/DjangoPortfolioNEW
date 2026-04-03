from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.prefetch_related("dev").all()
    return render(request, "projects_list.html", {"projects": projects})


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")