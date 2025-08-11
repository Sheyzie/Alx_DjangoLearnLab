from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


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