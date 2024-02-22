from django.contrib import admin

from .models import Author, Post, Comment

admin.site.register((Author, Post, Comment))
