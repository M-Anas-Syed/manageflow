import uuid


from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

from manageflow.accounts.models import User


class Board(models.Model):
    board_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Board")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    assigned_to = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.text


class BoardTask(models.Model):
    board = models.ForeignKey(Board, models.CASCADE, related_name="board")
    task = models.ForeignKey(Task, models.CASCADE)
