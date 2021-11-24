from django.contrib import admin

# Register your models here.
from .models import BlogPost, CommentPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    pass
