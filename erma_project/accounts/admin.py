from django.contrib import admin
from .models import Person

# Register your models here.
@admin.register(Person)
class AdminView(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'is_dev']
