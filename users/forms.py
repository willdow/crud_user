from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'date_of_birth', 'is_eating_healthy', 'is_playing_sport', 'is_intellectually_stimulated')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'date_of_birth', 'is_eating_healthy', 'is_playing_sport', 'is_intellectually_stimulated')