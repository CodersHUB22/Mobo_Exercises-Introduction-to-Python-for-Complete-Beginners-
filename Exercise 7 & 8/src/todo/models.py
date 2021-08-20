from django.db import models


class Todo(models.Model):
    todo_text = models.CharField(max_length=255)
    created_date = models.DateTimeField(null=True)
    modified_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.todo_text
