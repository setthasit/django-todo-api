from django.db import models
from django.db.models import fields
from rest_framework import serializers

from api.subtask.interfaces.dto import SubtaskDTO
from api.todo.model import Todo


class TodoDTO(serializers.ModelSerializer):
    subtasks = SubtaskDTO(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'status',
            'subtasks'
        )


class TodoUpdateDTO(serializers.Serializer):
    status = serializers.BooleanField(required=True)
