from django.shortcuts import render
from matcher_app.models import Job,Candidate,Skill,Match
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status
import json
from matcher_app.serializer import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get']

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username']

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    http_method_names = ['get', 'delete']

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ['get']
