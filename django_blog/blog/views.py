from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import CustomUserCreationForm, PostCreationForm, PostUpdateForm, CommentForm
from .models import Post, Comment, Tag


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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')

        return context

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

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'  # create this template
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        return Post.objects.filter(tags__name=self.tag.name).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

class SearchPostListView(ListView):
    model = Post
    template_name = 'blog/search_results.html'  # create this template
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        else:
            return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


# ------------------------------------
  
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog/post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form, 'post': post})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog/post_detail.html'
    form_class = PostCreationForm

    def form_valid(self, form):
        # Automatically assign the logged-in user as the author
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'comment_form.html'
    form_class = PostUpdateForm
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author

