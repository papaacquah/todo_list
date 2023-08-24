from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('name', 'description', 'completed')
    actions = ['completed', 'not_completed']



    def completed(self, request, queryset):
        queryset.update(completed=True)
    completed.short_description = 'Order completed'

    def not_completed(self, request, queryset):
        queryset.update(completed=False)
    not_completed.short_description = 'Order not completed'