from rest_framework import serializers
from api.todo.model import Todo

class TodoDAO(serializers.ModelSerializer):
    class Meta:
        model: Todo
        fields = (
            'id',
            'title',
            'status',
        )