from functools import partial
from rest_framework import generics, response
from rest_framework.decorators import api_view
from api.subtask.model import Subtask
from api.todo.interfaces.dao import TodoDAO

from api.todo.model import Todo
from api.todo.interfaces.dto import TodoDTO, TodoUpdateDTO


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by("id")
    serializer_class = TodoDTO


class TodoDetail(generics.RetrieveDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDTO


@api_view(["PATCH"])
def updateStatus(request, pk=None):
    validation = TodoUpdateDTO(data=request.data)
    if not validation.is_valid():
        return response.Response(validation.errors, status=400)

    # Define new status variable
    newStatus = request.data["status"]

    # Update Subtasks status
    Subtask.objects.filter(todo=pk).update(status=newStatus)

    # Update Todo status

    todo = generics.get_object_or_404(Todo, pk=pk)
    todoDAO = TodoDAO(instance=todo, data={"status": newStatus}, partial=True)
    if todoDAO.is_valid():
        todoDAO.save()
    else:
        return response.Response(todoDAO.errors, status=500)

    return response.Response(request.data, status=200)
