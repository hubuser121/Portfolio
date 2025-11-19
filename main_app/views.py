from django.shortcuts import render
from .models import AboutMe, Project, Certificate, Experience, Publication, LeadershipActivity, Skill, Education

def home(request):
    about_instance = AboutMe.objects.first()
    about_text = about_instance.content if about_instance else ""
    profile_url = about_instance.profile_image.url if about_instance and about_instance.profile_image else None
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    education = Education.objects.all().order_by('-start_date')
    publications = Publication.objects.all().order_by('-publication_date')
    leaderships = LeadershipActivity.objects.all().order_by('-start_date')

    context = {
        'about_text': about_text,
        'profile_url': profile_url,
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'education': education,
        'publications': publications,
        'leaderships': leaderships,
    }
    return render(request, 'main_app/home.html', context)

def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'main_app/certificates.html', {'certificates': certificates})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main_app/projects.html', {'projects': projects})
