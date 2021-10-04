from rest_framework import generics, serializers

from api.todo.model import Todo
from api.todo.interfaces.dto import TodoDTO

class TodoList(generics.ListCreateAPIView):
	queryset = Todo.objects.all().order_by("id")
	serializer_class = TodoDTO

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoDTO
