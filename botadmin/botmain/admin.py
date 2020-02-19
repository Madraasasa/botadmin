from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc',  'level']
    list_display_links = ['id', 'name', 'desc']


class UserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'name', 'lastname']
# Register your models here.


class DonateAdmin(admin.ModelAdmin):
    list_display = ['id', 'donate']


admin.site.register(Task, TaskAdmin)
admin.site.register(Button)
admin.site.register(User, UserAdmin)
admin.site.register(Donate, DonateAdmin)