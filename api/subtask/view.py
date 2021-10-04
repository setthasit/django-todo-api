from rest_framework import generics, serializers

from api.subtask.model import Subtask
from api.subtask.serializer import SubtaskSerializer

class SubtaskCreate(generics.CreateAPIView):
	queryset = Subtask.objects.all()
	serializer_class = SubtaskSerializer

class SubtaskDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subtask.objects.all()
	serializer_class = SubtaskSerializer
