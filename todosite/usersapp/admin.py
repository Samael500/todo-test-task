from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as ua
from django.contrib.auth.models import User

from todoapp.models import TaskList


class MyModelAdmin(admin.ModelAdmin):
    (add_form_template, change_user_password_template, fieldsets,
     add_fieldsets, form, add_form, change_password_form, list_display,
     list_filter, search_fields, ordering, filter_horizontal,) = (
     ua.add_form_template, ua.change_user_password_template, ua.fieldsets,
     ua.add_fieldsets, ua.form, ua.add_form, ua.change_password_form,
     ua.list_display, ua.list_filter, ua.search_fields, ua.ordering,
     ua.filter_horizontal, )

    list_display = ('username', 'is_staff', )


    def get_tasklists(self, object_id):
        tl = TaskList.objects.filter(user_id=object_id)
        for t in tl: t._number_of_tasks()
        return tl

    def change_view(self, request, object_id, form_url='', extra_context=None):
       extra_context = extra_context or {}
       extra_context['tasklists'] = self.get_tasklists(object_id)
       return super(MyModelAdmin, self).change_view(request, object_id,
           form_url, extra_context=extra_context)

admin.site.unregister(User)
admin.site.register(User, MyModelAdmin)
