from django.db.models import fields
from rest_framework import serializers
from api.subtask.model import Subtask

from api.todo import model

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = [
            'id',
            'title',
            'status'
        ]