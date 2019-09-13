from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

User = get_user_model()


class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    short_desc = models.TextField(max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    slug = models.SlugField(default='slug')
    is_published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def comments_list(self):
        return self.comments.filter(is_displayed=True)

    @property
    def total_comments(self):
        return self.comments_list.count()

    @property
    def author_full_name(self):
        try:
            return f'{author.first_name} {author.last_name}'
        except:
            return "name not set yet"

    class Meta:
        indexes = [models.Index(fields=['slug'])]
        ordering = ['-published_on']


@receiver(pre_save, sender=Post)
def upldate_published(sender, instance, **kwars):

    if instance.id:
        old_value = Post.objects.get(pk=instance.id).published_on
        if not old_value:
            instance.published_on = timezone.now()
