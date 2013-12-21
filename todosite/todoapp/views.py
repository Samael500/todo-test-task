from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.


from todoapp.models import Task

def index(request):
    taskslist = Task.objects.order_by('created')[:5]
    template = loader.get_template('../templates/todoapp/index.html')
    context = RequestContext(request, {
        'taskslist': taskslist,
    })
    return HttpResponse(template.render(context))

def detail(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)

def results(request, task_id):
    return HttpResponse("You're looking at the results of task %s." % task_id)


from todoapp.models import TaskList
#from todoapp.admin import MyUserAdmin


def usertasklists(request, user_id):
    tasklists = []
    for tl in TaskList.objects.all():
        if tl.user_id == int(user_id):
            tasklists.append(tl)

    template = loader.get_template('../templates/admin/base.html')
    
    context = RequestContext(request, {
        'tasklists': tasklists,
    })
    return HttpResponse(template.render(context))