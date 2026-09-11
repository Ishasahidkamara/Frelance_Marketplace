from django.contrib import admin
from .models import Project, ProjectAttachment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'freelancer', 'budget', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['title', 'client__username', 'freelancer__username']
    ordering = ['-created_at']


@admin.register(ProjectAttachment)
class ProjectAttachmentAdmin(admin.ModelAdmin):
    list_display = ['project', 'uploaded_by', 'uploaded_at']
