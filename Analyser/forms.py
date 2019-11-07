from django import forms
from Accounts import models
from django.contrib.auth.models import User
class HashtagForm(forms.ModelForm):
	class Meta:
		model = models.HashtagProfile
		fields = ['Hashtag_Searched']