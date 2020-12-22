from django.db import models


class Candidate(models.Model):
    username = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=512)
    skills = models.ManyToManyField('Skill', related_name ='candidates', blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=512)
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=512)
    skill = models.ForeignKey('Skill', related_name ='jobs', on_delete=models.CASCADE)
    def __str__(self):
        return '{} ({})'.format(self.title, self.skill.name)

class Match(models.Model):
    job = models.ForeignKey('Job', related_name ='matches', on_delete=models.CASCADE)
    candidate = models.ForeignKey('Candidate', related_name ='matches', on_delete=models.CASCADE)
    reason = models.CharField(max_length=512, null=True)
    def __str__(self):
        return '{} - {}'.format(self.job.title, self.candidate.title)