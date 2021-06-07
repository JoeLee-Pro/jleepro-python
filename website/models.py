from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class FeaturedManager(models.Manager):
    def get_queryset(self):
        return super(FeaturedManager, self).get_queryset().filter(status='featured')


class Card(models.Model):
    STATUS_CHOICES = (
        ('other', 'Other'),
        ('featured', 'Featured'),
    )

    image_path = models.CharField(max_length=250)
    image_alt = models.CharField(max_length=250)
    title_icon = models.CharField(max_length=20)
    title = models.CharField(max_length=250)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='website_card'
    )

    body = models.TextField()
    button_text = models.CharField(max_length=20)
    link_path = models.CharField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='other'
    )

    objects = models.Manager()
    featured = FeaturedManager()

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title

