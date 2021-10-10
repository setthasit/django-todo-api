from django.shortcuts import get_object_or_404
from rest_framework import generics, response, viewsets
from rest_framework.decorators import action
from api.subtask.interfaces.dao import SubtaskDAO
from api.subtask.model import Subtask
from api.subtask.interfaces.dto import SubtaskDTO
from api.todo.interfaces.dao import TodoDAO
from api.todo.model import Todo

class SubtaskCreate(generics.CreateAPIView):
	queryset = Subtask.objects.all()
	serializer_class = SubtaskDTO

class SubtaskDetail(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskDTO

    @action(detail=True, methods=['patch'])
    def updateStatus(self, request, pk=None):
        # Update subtask status
        subtask = self.get_object()
        newStatus = request.data['status']
        subtaskDAO = SubtaskDAO(instance=subtask, data={ "status": newStatus }, partial=True)
        if subtaskDAO.is_valid():
            subtaskDAO.save()
        else:
            return response.Response(subtaskDAO.errors, status=500)

        # Update todo status
        todo = get_object_or_404(Todo, pk=request.data['todo'])
        if newStatus == False:
            todoDAO = TodoDAO(todo, data={ "status": newStatus }, partial=True)
            if todoDAO.is_valid():
                todoDAO.save()
            else:
                return response.Response(todoDAO.errors, status=500)
        elif newStatus == True:
            subtasks = Subtask.objects.filter(todo=request.data['todo'], status=False)
            if len(subtasks) == 0:
                todoDAO = TodoDAO(todo, data={ "status": newStatus }, partial=True)
                if todoDAO.is_valid():
                    todoDAO.save()
                else:
                    return response.Response(todoDAO.errors, status=500)

        return response.Response()
