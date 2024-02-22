from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)


    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
    
    
    # user being the most used model field through the web app
    class Meta:
        indexes = [
            models.Index(fields=['username'])
        ]
    



    """
    groups and permissions must be manually set up since we are no longer using the default
    Django's User model which has group and persmission pre-emptively defiend 

    """

    groups = models.ManyToManyField(
    Group,
    verbose_name=('groups'),
    blank=True,
    help_text=(
        'The groups this user belongs to. A user will get all permissions '
        'granted to each of their groups.'
    ),
    related_name="customuser_set",
    related_query_name="user",
)


    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="customuser_set",
        related_query_name="user",
    )
