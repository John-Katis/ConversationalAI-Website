from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='ConversationalAI-Home'),
    path('research_objectives', views.research_objectives, name='ConversationalAI-Research-Objectives'),
    path('research_approach', views.research_approach, name='ConversationalAI-Research-Approach'),
    path('learning_design', views.learning_design, name='ConversationalAI-Learning-Design'),
    path('results', views.results, name='ConversationalAI-Results'),
    path('project_team', views.project_team, name='ConversationalAI-Project-Team')
]
