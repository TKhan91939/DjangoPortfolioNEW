from django.shortcuts import render
from .models import Project, Resume, AboutPage

def project_list(request):
    projects = Project.objects.prefetch_related("dev").all()
    return render(request, "projects_list.html", {"projects": projects})


def about(request):
    about_obj = AboutPage.objects.filter(is_active=True).order_by("-updated_at").first()
    return render(request, "about.html", {"about_obj": about_obj})

def contact(request):
    return render(request, "contact.html")

def resume(request):
    resume_obj = Resume.objects.filter(is_active=True).order_by("-updated_at").first()
    return render(request, "resume.html", {"resume_obj": resume_obj})

