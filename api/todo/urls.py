from django.urls import path
from api.todo.view import TodoDetail, TodoList, updateStatus

urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>/', TodoDetail.as_view()),
    path('<int:pk>/status', updateStatus),
]
