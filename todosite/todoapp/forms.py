from django.db import models
from django import forms

from todoapp.models import *

class TLForm(forms.ModelForm):
    class Meta:
        model = TaskList
        #title = forms.CharField(max_length=140)
        exclude = ('user',)

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        #subject = forms.CharField(max_length=140)
        fields = ('subject',)

class TaskForm(forms.ModelForm):

    def __init__ (self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        user_id = kwargs['instance'].user_id
        #print user_id
        #self.subject = forms.CharField(max_length=140)
        qs = TaskList.objects.filter(user_id=user_id)
        self.base_fields['tl'] = forms.ModelChoiceField(queryset=qs , empty_label=None)

    class Meta:
        model = Task
        exclude = ('user', )

