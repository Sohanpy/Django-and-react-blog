from django.contrib.auth import get_user_model
from rest_framework import serializers

from user_profile.models import UserProfile

User = get_user_model()


class AdminListSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_superuser'
        ]
