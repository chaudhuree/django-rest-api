from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_body', 'created_at', 'updated_at')
    search_fields = ('blog_title', 'blog_body')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'blog', 'created_at', 'updated_at')
    search_fields = ('blog', 'comment')