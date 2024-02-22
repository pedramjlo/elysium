from django.urls import path

from .views import create_post, Feed, PostPage, AllTag, TagDetail
from user_account.views import out




urlpatterns = [
    path("create_post/", create_post, name='create_post'),
    path("feed/", Feed.as_view(), name='feed'),
    path("post/<int:pk>", PostPage.as_view(), name='post'),
    path("tags/", AllTag.as_view(), name='tags'),
    path('tags/<slug:slug>/', TagDetail.as_view(), name='tag_detail'),
    

]