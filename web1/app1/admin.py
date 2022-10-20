from django.contrib import admin
from .models import Movies, Report, Student

admin.site.register(Movies)
#adminview to create adminview
@admin.register(Student)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('rollno','klass','name')
    search_fields = ('name','klass')
    ordering = ('name',)

@admin.register(Report)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('student','english','hindi','maths','science')
# Register your models here.
