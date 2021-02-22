from django.contrib import admin
from .models import Works
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title and Date", {"fields": ["Name", "PublishDate"]}),
        ("content",{"fields":["Description"]})
    ]
    formfield_overrides ={
        models.TextField : {'widget': TinyMCE()}
    }

admin.site.register(Works, WorkAdmin)
