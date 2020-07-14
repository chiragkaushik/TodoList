from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.user)
admin.site.register(models.TodoList)
admin.site.register(models.Access)
admin.site.register(models.TodoItem)

