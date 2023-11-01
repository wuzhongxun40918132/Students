from django.contrib import admin
from .models import Student  

class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter = ('cSex',)

admin.site.register(Student, studentAdmin)