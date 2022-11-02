from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'ConvAIWebsite/homepage.html')


def research_objectives(request):
    return render(request, 'ConvAIWebsite/researchObjectives.html')


def research_approach(request):
    return render(request, 'ConvAIWebsite/researchApproach.html')


def learning_design(request):
    return render(request, 'ConvAIWebsite/learningDesign.html')


def results(request):
    return render(request, 'ConvAIWebsite/results.html')


def project_team(request):
    return render(request, 'ConvAIWebsite/projectTeam.html')

