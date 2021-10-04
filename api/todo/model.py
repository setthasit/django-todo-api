from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} {self.status}"
