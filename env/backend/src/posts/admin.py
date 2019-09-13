from django.contrib import admin

# Register your models here.
from comments.models import Comment
from .models import Post


class CommentInLine(admin.StackedInline):
    model = Comment


class PosADmin(admin.ModelAdmin):

    def post_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()

    post_comment_count.short_desc = 'Total Comments'

    inlines = [
        CommentInLine
    ]
    list_display = ['title', 'author', 'is_published', 'post_comment_count']


admin.site.register(Post)
