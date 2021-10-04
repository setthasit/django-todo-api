from rest_framework import serializers

from api.subtask.interfaces.dto import SubtaskDTOSerializer
from api.todo.model import Todo

class TodoDTO(serializers.ModelSerializer):
    subtasks = SubtaskDTOSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'status',
			'subtasks'
        )
