from django.contrib import admin

from api.todo.model import Todo
from api.subtask.model import Subtask

admin.site.register(Todo)
admin.site.register(Subtask)