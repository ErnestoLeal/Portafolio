from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def experience(request):
    return render(request, 'core/experience.html')

def skills(request):
    return render(request, 'core/skills.html')

def contactme(request):
    return render(request, 'core/contactme.html')
