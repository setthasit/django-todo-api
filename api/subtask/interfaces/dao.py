from rest_framework import serializers
from api.subtask.model import Subtask

class SubtaskDAO(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = [
            'id',
            'title',
            'status',
        ]
