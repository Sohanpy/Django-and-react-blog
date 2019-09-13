from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    websites = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username


@receiver(post_save, sender=User)
def user_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
