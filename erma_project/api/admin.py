from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdminView(admin.ModelAdmin):
    list_display = [ 'title' , 'project_manager' , 'developer' , 'progress'] 