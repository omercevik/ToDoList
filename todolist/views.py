import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ToDoList, ToDoLists
from .forms import ToDoListForm, ToDoListsForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone


@login_required
def lists(request):
    if request.method == 'POST':
        form = ToDoListsForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = ToDoLists.objects.all
            messages.success(request, 'New To Do List is Created')
            return render(request, "lists.html", {'all_items': all_items})
        else:
            messages.error(request, 'Error: There is an error while creating new list!')
            return redirect('lists')
    else:
        all_items = ToDoLists.objects.all
        return render(request, 'lists.html', {'all_items': all_items})


@login_required
def todolist(request, list_id):
    if request.method == 'POST':
        form = ToDoListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = checkDate(list_id)
            listName = ToDoLists.objects.get()
            messages.success(request, 'Item is added to list')
            return render(request, "todolist.html", {'all_items': all_items, 'list_id': list_id})
        else:
            messages.error(request, 'Error: There is an error while adding item to list!')
            return redirect('todolist', list_id)
    else:
        all_items = checkDate(list_id)
        return render(request, 'todolist.html', {'all_items': all_items, 'list_id': list_id})


def checkDate(list_id):
    all_items = ToDoList.objects.filter(listId=list_id)
    for i in all_items.all():
        if datetime.datetime.strptime(str(i.deadline)[:10], '%Y-%m-%d') < datetime.datetime.now():
            i.status = 2
            i.save()
    return all_items


@login_required
def order(request, list_id, order_by_what):
    items = ToDoList.objects.filter(listId=list_id)
    items = items.order_by(order_by_what)
    return render(request, 'todolist.html', {'all_items': items, 'today': timezone.now(), 'list_id': list_id})


def delete(request, list_id, returnId):
    item = ToDoList.objects.get(pk=list_id)
    item.delete()
    messages.success(request, '\'' + item.itemName + '\' is deleted!')
    return redirect('todolist', returnId)


def delete_list(request, list_id):
    item = ToDoLists.objects.get(pk=list_id)
    item.delete()
    items = ToDoList.objects.filter(listId=list_id)
    items.delete()
    messages.success(request, '\'' + item.todoListName + '\' is deleted!')
    return redirect('lists')


def cross_off(request, list_id, returnId):
    item = ToDoList.objects.get(pk=list_id)
    item.status = 1
    item.save()
    return redirect('todolist', returnId)


def uncross(request, list_id, returnId):
    item = ToDoList.objects.get(pk=list_id)
    item.status = 0
    item.save()
    return redirect('todolist', returnId)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def login(request):
    return render(request, "registration/login.html", {})


def home(request):
    return render(request, "home.html", {})


def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
