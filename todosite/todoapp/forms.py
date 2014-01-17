from django.db import models
from django import forms

from todoapp.models import *

class TLForm(forms.ModelForm):
    class Meta:
        model = TaskList
        title = forms.CharField(max_length=140)
        exclude = ('user',)

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        subject = forms.CharField(max_length=140)
        fields = ('subject',)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        subject = forms.CharField(max_length=140)
        exclude = ('user',)

