from rest_framework import serializers

from comments.models import Comment


class CommentsListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'website',
            'body',
            'post',
            'is_displayed',
            'published_on'
        ]


class CommentCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'website',
            'body',
            'post',
            'is_displayed',
        ]
