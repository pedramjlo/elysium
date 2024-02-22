from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from blog.models import Author  # assuming your Author model is in the blog app

@receiver(post_save, sender=CustomUser)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(author=instance)
