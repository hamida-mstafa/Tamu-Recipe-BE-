from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

class ProfileForm(forms.ModelForm):
    '''
    class to define profile form
    '''
    class Meta:
        model = Profile
        exlcude = ['user']
        fields = ('bio', 'profile_pic','contacts')

class UpdateProfile(forms.ModelForm):
    '''
    class to define updateprofile form
    '''
    class Meta:
        model = Profile
        fields = ['profile_pic','bio']                