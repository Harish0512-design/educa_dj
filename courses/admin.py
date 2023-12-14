from django.contrib import admin
from .models import Subject, Course, Module, Content, Text, File, Image, Video

# Register your models here.
admin.site.register(Subject)
admin.site.register(Content)
admin.site.register(Text)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Video)


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on']
    list_filter = ['created_on', 'updated_on', 'subject']
    search_fields = ['subject', 'owner', 'overview']
    inlines = [ModuleInline]
