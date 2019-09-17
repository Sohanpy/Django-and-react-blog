from rest_framework import serializers

from posts.models import Post
from api.comments.serializers import CommentsListSerializers


class PostDetailsSerializers(serializers.ModelSerializer):

    comments = CommentsListSerializers(many=True)
    author_full_name = serializers.CharField()
    total_comments = serializers.IntegerField()

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'short_desc',
            'author',
            'author_full_name',
            'slug',
            'comments',
            'is_published',
            'created_on',
            'published_on',
            'last_edited',
            'total_comments',
            'images'
        ]


class PostsSerializers(serializers.ModelSerializer):

    author_full_name = serializers.CharField()
    total_comments = serializers.IntegerField()

    class Meta:
        model = Post
        fields = [
            'title',
            'short_desc',
            'author',
            'author_full_name',
            'slug',
            'is_published',
            'created_on',
            'published_on',
            'last_edited',
            'total_comments',
            'images'

        ]
