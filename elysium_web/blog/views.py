from django.shortcuts import render, redirect

from .models import Author, Post, Comment
from .forms import CreatePost, CommentForm
from taggit.models import Tag




from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin




class Feed(ListView):
    model = Post
    template_name = 'blog/feed.html'
    paginate_by = 10

    def get_queryset(self):
        ordering = self.request.GET.get('sort', '-date_created')
        return Post.objects.all().order_by(ordering)
    


    


class PostPage(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post)

        if comments.exists():
            context['comments'] = comments
        else:
            context['comments'] = None

        context['form'] = CommentForm()

        return context
    

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            
            if request.user.is_authenticated:
                comment.commetor = request.user  # Set the commetor to the current user if they are authenticated
            comment.save()
        return redirect(request.path)  # Return the HttpResponseRedirect object

    
    
    




@login_required
def create_post(request, *args, **kwargs):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']

            if title.strip() != " " and content.strip() != " ":
                author = Author.objects.get(author=request.user)
                post = Post.objects.create(title=title, content=content, author=author)
                post.tags.add(*tags)
                post.save()
                return redirect(f'/feed')
            else:
                return form.add_error("title", "content", "Title or Content fields cannot be empty!")
    else:
        form = CreatePost()

    context = {
        'form': form,
        'username': request.user.username,
    }

    return render(request, 'blog/create.html', context)




class AllTag(ListView):
    model = Post
    template_name = 'blog/tags.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context




class TagDetail(DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.get_object()
        context['posts'] = Post.objects.filter(tags__name=tag)
        return context