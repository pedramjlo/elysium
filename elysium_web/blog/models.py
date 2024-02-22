from django.db import models
from taggit.managers import TaggableManager

from user_account.models import CustomUser



from user_account.models import CustomUser



class Author(models.Model):
    author = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.author.username



class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=80, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-date_created']


    def __str__(self):
        return f"{self.title} by ({self.author})"
    

    






class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    commetor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    comment_body = models.TextField(max_length=300, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        
        if len(self.comment_body.split()) > 4:
            res = " ".join(self.comment_body.split(" ")[:5])
        else:
            res = " ".join(self.comment_body.split(" ")[:4])

        return res + "..."




