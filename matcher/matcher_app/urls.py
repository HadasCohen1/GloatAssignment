from matcher_app.views import CandidateViewSet,JobViewSet,MatchViewSet,SkillViewSet
from django.conf.urls import  url, include
from rest_framework import routers


api_router = routers.DefaultRouter()
api_router.register(r'candidate', CandidateViewSet, basename='candidate')
api_router.register(r'job', JobViewSet, basename='job')
api_router.register(r'skill', SkillViewSet, basename='skill')
api_router.register(r'match', MatchViewSet, basename='match')


api_urls=api_router.urls