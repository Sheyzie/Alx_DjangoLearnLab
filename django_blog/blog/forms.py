from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget

from .models import Post, Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", 'tags')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        field = ("title", "content", 'tags')
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        field = ("content")
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control'}),
        }