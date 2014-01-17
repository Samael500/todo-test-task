from django.contrib import admin

# Register your models here.

from todoapp.models import Task
from todoapp.models import TaskList

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["subject", "status"]}),
        ("User info", {"fields": ["tl", "user"], "classes": ["collapse"]}),
        #("Date info", {"fields": ["created"]}),
    ]
    
    list_display = ["subject", "user", "tl", "created", "status"]
    
    search_fields = ["subject"]
    list_filter = ["created", "status", "user"]

    date_hierarchy = "created"

class TaskListAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

    list_display = ["title", "created", "user", "_number_of_tasks"]

    search_fields = ["title"]
    list_filter = ["created", "number_of_tasks"]

    date_hierarchy = "created"

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)
