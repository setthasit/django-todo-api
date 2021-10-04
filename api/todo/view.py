from rest_framework import generics, serializers

from api.todo.model import Todo
from api.todo.interfaces.dto import TodoDTOSerializer

class TodoList(generics.ListCreateAPIView):
	queryset = Todo.objects.all().order_by("id")
	serializer_class = TodoDTOSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoDTOSerializer
