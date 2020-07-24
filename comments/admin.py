from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin panel for Comment model"""
    fieldsets = [
        ('Commenter', {'fields': ['commenter']}),
        ('Content', {'fields': ['content']}),
        ('post', {'fields': ['post']}),
        ('Reply to', {'fields': ['reply_to']}),
    ]
    list_display = ('commenter', 'post', 'content', 'reply_to', 'date_created')
    search_fields = ['content']
