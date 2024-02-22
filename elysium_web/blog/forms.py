from django import forms

from .models import Post, Comment


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'post-title-field'}),
            'content': forms.Textarea(attrs={'class': 'post-content-field'}),
            'tags': forms.Textarea(attrs={'class': 'post-tags-field'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =  ('comment_body',)