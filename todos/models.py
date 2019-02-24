from django.db import models

# Create your models here.


class Todo(models.Model):
    text = models.TextField()
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    is_due_today = models.BooleanField(default=False)
    is_due_tomorrow = models.BooleanField(default=False)
