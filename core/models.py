from django.db import models

# Create your models here.
class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    img = models.ImageField(upload_to="devs/")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        managed = True
        verbose_name = "Developer"
        verbose_name_plural = "Developers"





class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    img = models.ImageField(upload_to="projects/")
    date = models.DateField(auto_now_add=True)
    link = models.URLField(null=True, blank=True)
    gist = models.URLField(null=True, blank=True)
    git_id = models.IntegerField(unique=True, null=True, blank=True)
    dev = models.ManyToManyField(Developer, related_name="developers")

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        verbose_name = "Project"
        verbose_name_plural = "Projects"

# List display 
# Jazmin 
# drf

class Resume(models.Model):
    title = models.CharField(max_length=150, default="My Resume")
    linkedin_url = models.URLField(blank=True, null=True)
    resume_pdf = models.FileField(upload_to="resumes/")
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"


class AboutPage(models.Model):
    title = models.CharField(max_length=150, default="About Me")
    bio = models.TextField()
    favorite_movie = models.CharField(max_length=150, blank=True, null=True)
    favorite_food = models.CharField(max_length=150, blank=True, null=True)
    interests = models.TextField(blank=True, null=True, help_text="Enter one interest per line.")
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = "About Page"
        verbose_name_plural = "About Page"