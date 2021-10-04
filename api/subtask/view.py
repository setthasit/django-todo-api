from rest_framework import generics

from api.subtask.model import Subtask
from api.subtask.interfaces.dto import SubtaskDTO

class SubtaskCreate(generics.CreateAPIView):
	queryset = Subtask.objects.all()
	serializer_class = SubtaskDTO

class SubtaskDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subtask.objects.all()
	serializer_class = SubtaskDTO
