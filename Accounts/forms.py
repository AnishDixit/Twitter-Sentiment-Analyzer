from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CreateProfile(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['First_Name', 'Last_Name', 'Age', 'Profile_Pic']

class UpdateProfile(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['First_Name', 'Last_Name', 'Age', 'Profile_Pic']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
    	model = User
    	fields = ['username', 'email', 'password1', 'password2']