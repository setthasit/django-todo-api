from rest_framework import generics

from api.subtask.model import Subtask
from api.subtask.interfaces.dto import SubtaskDTOSerializer

class SubtaskCreate(generics.CreateAPIView):
	queryset = Subtask.objects.all()
	serializer_class = SubtaskDTOSerializer

class SubtaskDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subtask.objects.all()
	serializer_class = SubtaskDTOSerializer
