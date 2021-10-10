from django.urls import path

from api.subtask.view import SubtaskCreate, SubtaskDetail

urlpatterns = [
    path('', SubtaskCreate.as_view()),
    path('<int:pk>/status', SubtaskDetail.as_view({ 'patch': 'updateStatus' })),
]