from django.contrib.auth import get_user_model
from rest_framework import serializers

from user_profile.models import UserProfile

User = get_user_model()


class UserProfileSerializers(serializers.ModelSerializer):

    websites = serializers.URLField(
        source='profile.websites', allow_blank=True, allow_null=True
    )

    bio = serializers.CharField(
        source='profile.bio', allow_blank=True, allow_null=True
    )

    facebook = serializers.URLField(
        source='profile.facebook', allow_blank=True, allow_null=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'websites',
            'bio',
            'facebook'
        ]

    def update(self, instance, validated_data):

        profile_data = validated_data.pop('profile', None)
        self.update_or_create_profile(instance, profile_data)
        return super(UserProfileSerializers, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        UserProfile.objects.update_or_create(user=user, defaults=profile_data)


class UserStatus(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'is_active',
            'is_superuser'
        ]
