from rest_framework import serializers
from matcher_app.models import Job,Candidate,Skill,Match


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class JobSerializer(serializers.HyperlinkedModelSerializer):
    skill = SkillSerializer()
    
    class Meta:
        model = Job
        fields = "__all__"
class MatchSerializer(serializers.HyperlinkedModelSerializer):
    job=JobSerializer()
    id = serializers.IntegerField()

    class Meta:
        model = Match
        fields = '__all__'

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    skills = SkillSerializer(many=True)
    matches = MatchSerializer(many=True)
    class Meta:
        model = Candidate
        fields = '__all__'

