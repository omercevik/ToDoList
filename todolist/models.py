from django.db import models
from django.utils import timezone


class ToDoList(models.Model):
    listId = models.IntegerField(default=0)
    itemName = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=400, default="")
    status = models.IntegerField(default=0)
    deadline = models.DateTimeField(default=timezone.now)
    createdDate = models.DateTimeField(default=timezone.now)


class ToDoLists(models.Model):
    userId = models.IntegerField(default=0)
    todoListName = models.CharField(max_length=200, default="")

