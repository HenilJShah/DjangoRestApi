from django.contrib import admin

# Register your models here.
from filteringApp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'city', 'passby')


admin.site.register(Student, StudentAdmin)
