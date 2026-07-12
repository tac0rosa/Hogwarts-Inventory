from django.contrib import admin

from .models import House, Professor, Student, Item

admin.site.register(House)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Item)
