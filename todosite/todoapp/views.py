from django.shortcuts import render

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from todoapp.models import *
from todoapp.forms import *

# Create your views here.

@login_required
def index(request):

    tl = TaskList.objects.filter(user_id=request.user.id)
    for t in tl: t._number_of_tasks()

    free = len (Task.objects.filter(user_id=request.user.id, tl_id=None))

    form = TLForm()

    return render(request, 'todoapp/index.html', {'tasklists': tl, 'free': free, 'form':form,}, )

@login_required
def detail(request, tasklist_id = None):
    if tasklist_id: tl = get_object_or_404(TaskList, user_id=request.user.id, pk=tasklist_id)
    else: tl = None
    tls = Task.objects.filter(user_id=request.user.id, tl_id=tasklist_id )

    form = AddTaskForm()

    return render(request, 'todoapp/detail.html', {'tasks': tls, 'form':form, 'tl':tl,}, )

@login_required
def addtl(request):
    if request.method == 'POST':
        tl = TaskList(user_id=request.user.id)
        form = TLForm(request.POST, instance=tl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:index'))
    else:
        form = TLForm()
    return HttpResponseRedirect(reverse('todoapp:index'))

@login_required
def deltl(request, tasklist_id ):
    tl = get_object_or_404(TaskList, pk=tasklist_id, user_id=request.user.id)
    tl.delete()
    #task.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

@login_required
def deltask(request, task_id ):
    task = get_object_or_404(Task, pk=task_id, user_id=request.user.id)
    task.delete()
    #task.save()
    return HttpResponseRedirect(reverse('todoapp:detail', args=(task.tl.id,)))

@login_required
def change(request, task_id ):
    task = get_object_or_404(Task, pk=task_id, user_id=request.user.id)
    task.status = not task.status
    task.save()
    return HttpResponseRedirect(reverse('todoapp:detail', args=(task.tl.id,)))

@login_required
def addtask(request, tasklist_id ):
    if request.method == 'POST':
        task = Task(user_id=request.user.id, tl_id=tasklist_id)
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:detail', args=(task.tl.id,) ))
    else:
        form = AddTaskForm()
    return HttpResponseRedirect(reverse('todoapp:detail', args=(task.tl.id,) ))

@login_required
def changetl(request, tasklist_id ):
    tl = get_object_or_404(TaskList, user_id=request.user.id, pk=tasklist_id)

    if request.method == 'POST':
        form = TLForm(request.POST, instance=tl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:detail', args=(tl.id,) ))
    else:
        form = TLForm(instance=tl)
    return render(request, 'todoapp/change_tl.html',{'form': form, 'tl':tasklist_id,})

@login_required
def changetask(request, task_id ):
    task = get_object_or_404(Task, user_id=request.user.id, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            if task.tl_id: path = reverse('todoapp:detail', args=(task.tl_id,))
            else: path = reverse('todoapp:detail')
            return HttpResponseRedirect(path)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/change_task.html',{'form': form, 'task':task_id,})
