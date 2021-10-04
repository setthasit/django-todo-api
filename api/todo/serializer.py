from django.db.models import fields
from rest_framework import serializers

from api.subtask.serializer import SubtaskSerializer
from .model import Todo

class TodoSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'status',
			'subtasks'
        )
