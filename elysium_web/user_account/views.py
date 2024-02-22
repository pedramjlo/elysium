from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DetailView

from blog.models import *
from .models import CustomUser
from .forms import RegisterForm, LoginForm
from taggit.models import Tag



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user instance yet
            user.set_password(form.cleaned_data['password1'])  # Set the password
            user.save()  # Now save the user instance

            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/feed')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})





def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # If the user is authenticated then login and redirect to home page
            if user is not None:
                login(request, user)
                return redirect('/feed')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def out(request):
    logout(request)
    return redirect('/login')



class ProfileView(DetailView):
    model = CustomUser
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        full_name = f"{user.first_name} {user.last_name}"
        author = Author.objects.get(author=user)
        context['posts'] = Post.objects.filter(author=author).order_by('-date_created')[:5]
        context['full_name'] = full_name
        return context

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        if "delete_posts" in request.POST:
            author = Author.objects.get(author=user)
            Post.objects.filter(author=author).delete()
            return redirect('profile', pk=user.pk)

        elif "delete_account" in request.POST:
            user.delete()
            logout(request)
            return redirect('/register')
