from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from taggit.models import Tag  
from .models import Author, Post



@receiver(post_save, sender=get_user_model())
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(author=instance)


@receiver(post_delete, sender=Post)
def remove_unused_tags(sender, instance, **kwargs):
    for tag in Tag.objects.all():
        if not tag.taggit_taggeditem_items.exists():
            tag.delete()
