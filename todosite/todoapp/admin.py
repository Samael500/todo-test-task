from django.contrib import admin

# Register your models here.

from todoapp.models import Task
from todoapp.models import TaskList
#from models import User

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# from models import DateTime

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["subject", "status"]}),
        ("User info", {"fields": ["tasklist", "user"], "classes": ["collapse"]}),
        #("Date info", {"fields": ["created"]}),
    ]
    
    list_display = ["subject", "user", "tasklist", "created", "status"]
    
    search_fields = ["subject"]
    list_filter = ["created", "status", "user"]

    date_hierarchy = "created"

class TaskListAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

    list_display = ["title", "created", "user", "_number_of_tasks"]

    search_fields = ["title"]
    list_filter = ["created", "number_of_tasks"]

    date_hierarchy = "created"


class MyUserAdmin(UserAdmin):

    fields = ("username", "password", "email", "tasklists")

    fieldsets = None

    readonly_fields = ("username", "tasklists",)
    
    def tasklists(self, obj):
        return str(obj) + " url ../admin/auth/user/" + str(obj.id) + "/tasklists"

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)