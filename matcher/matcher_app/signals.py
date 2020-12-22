# coding=utf-8
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from matcher_app.models import Job,Candidate
from matcher_app.candidate_finder import find_candidates_for_job,find_jobs_for_candidate

@receiver(post_save, sender=Job)
def job_create(sender, instance, raw, created, using, update_fields, **kwargs):
    if created:
        find_candidates_for_job(instance)

@receiver(m2m_changed, sender=Candidate.skills.through)
def candidate_skill_change(sender, action, instance, **kwargs):
    if action == 'post_add':
        find_jobs_for_candidate(instance)
