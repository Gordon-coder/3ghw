from django.contrib import admin
from .models import *

# Register your models here.
class AssigmentAdmin(admin.ModelAdmin):
    list_display = ['date', 'subject', 'obj']
    list_filter = ['date', 'subject']

admin.site.register(Assignment, AssigmentAdmin)