from matcher_app.models import Skill, Job, Candidate,Match
import re
from django.db.models import Q

def create_match(job,candidate):
    """
    crate match object
    :param job: job object
    :param candidate: candidate object
    """
    reason = 'Requires "{}" skill and matches "{}" job title'.format(job.skill.name, job.title)
    match = Match(job=job, candidate=candidate, reason=reason)
    match.save()

def create_title_query(title):
    """
    create title filter 
    """
    query = Q()
    # split the title
    for entry in re.split('\W', title):
        query = query | Q(title__icontains=entry)
    return query

def find_candidates_for_job(job):
    """
    search matching candidates for specific job
    :param job: job object
    """
    query = create_title_query(job.title) & Q(skills__in=[job.skill])
    matching_candidates = Candidate.objects.filter(query)
    for candidate in matching_candidates:
        create_match(job,candidate)

def find_jobs_for_candidate(candidate):
    """
    search matching jobs for specific candidate
    :param job: candidate object
    """
    query = create_title_query(candidate.title) & Q(skill__id__in=candidate.skills.all())
    matching_jobs = Job.objects.filter(query)
    for job in matching_jobs:
        create_match(job,candidate)
