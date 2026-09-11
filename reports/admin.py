from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['reporter', 'reported_user', 'reason', 'status', 'created_at']
    list_filter = ['status', 'reason']
    search_fields = ['reporter__username', 'reported_user__username']
    ordering = ['-created_at']
