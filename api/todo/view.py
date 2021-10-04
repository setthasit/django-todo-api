from rest_framework import generics, serializers

from api.todo.model import Todo
from api.todo.serializer import TodoSerializer

class TodoList(generics.ListCreateAPIView):
	queryset = Todo.objects.all().order_by("id")
	serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
