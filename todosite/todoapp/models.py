from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    subject = models.CharField(max_length=140, default='New task')
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    tl = models.ForeignKey('TaskList', null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.subject)

class TaskList(models.Model):
    title = models.CharField(max_length=140, default='New task list')
    created = models.DateTimeField(auto_now_add=True)

    number_of_tasks = models.IntegerField(default=0, editable=False)

    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)

    def _number_of_tasks(self):
        self.number_of_tasks = 0
        task = Task.objects.filter(tl_id=self.id)
        self.number_of_tasks = len(task)
        self.save()
        return self.number_of_tasks