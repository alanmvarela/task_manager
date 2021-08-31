"""
serializers.py contains all the serializers used by the api.
"""

from rest_framework.serializers import ModelSerializer
from tasks.models import IssueCard, BugCard, TaskCard


class IssueCardSerializer(ModelSerializer):
    class Meta:
        model = IssueCard
        fields = ['title', 'description']


class BugCardSerializer(ModelSerializer):
    class Meta:
        model = BugCard
        fields = ['description']


class TaskCardSerializer(ModelSerializer):
    class Meta:
        model = TaskCard
        fields = ['title', 'category']


