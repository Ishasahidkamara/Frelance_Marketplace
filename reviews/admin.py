from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['project', 'client', 'freelancer', 'rating', 'created_at']
    list_filter = ['rating']
    search_fields = ['client__username', 'freelancer__username']
    ordering = ['-created_at']
