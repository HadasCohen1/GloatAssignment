from django.contrib import admin

# Register your models here.
from matcher_app.models import Skill,Job,Candidate,Match


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

    
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    search_fields = ['job__title']