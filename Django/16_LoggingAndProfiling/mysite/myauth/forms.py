from .models import Profile, User
from django import forms

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'avatar']
