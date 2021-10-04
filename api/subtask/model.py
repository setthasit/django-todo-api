from django.db import models

from api.todo.model import Todo

class Subtask(models.Model):
    title = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    todo = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
		related_name='subtasks'
    )

    def __str__(self) -> str:
        return f'{self.title} {self.status}'
