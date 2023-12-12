from django.contrib import admin
from . models import Subject, Course, Module

# Register your models here.
admin.site.register(Subject)


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on']
    list_filter = ['created_on', 'updated_on', 'subject']
    search_fields = ['subject', 'owner', 'overview']
    inlines = [ModuleInline]
