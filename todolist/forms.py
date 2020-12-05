from django import forms
from todolist.models import ToDoList, ToDoLists


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["listId", "itemName", "description", "deadline", "status"]


class ToDoListsForm(forms.ModelForm):
    class Meta:
        model = ToDoLists
        fields = ["userId", "todoListName"]

