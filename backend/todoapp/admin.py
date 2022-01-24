from django.contrib import admin
from .models import Todo #importing to do class

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")

    # Register Model

admin.site.register(Todo, TodoAdmin) #Crud Operations
