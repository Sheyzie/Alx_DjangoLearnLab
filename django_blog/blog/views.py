from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, PostCreationForm, PostUpdateForm
from .models import Post


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the new user
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # or wherever you want
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'blog/profile.html'
    context_object_name = 'user'

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'blog/edit_profile.html'
    success_url = reverse_lazy('profile')  

    def get_object(self):
        # Ensure users can only edit their own profile by ignoring the URL parameters and looking up the user from the request
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile was updated successfully.')
        return super().form_valid(form)
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostCreationForm

    def form_valid(self, form):
        # Automatically assign the logged-in user as the author
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'content']
    form_class = PostUpdateForm
    success_url = reverse_lazy('post_list')  # or whatever URL you want after updating

    def get_queryset(self):
        # Restrict queryset to posts owned by the logged-in user
        return Post.objects.filter(author=self.request.user)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        # Restrict queryset to posts owned by the logged-in user
        return Post.objects.filter(author=self.request.user)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author


