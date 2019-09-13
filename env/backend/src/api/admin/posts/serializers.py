from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post


class AdminDetailsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class AdminListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
