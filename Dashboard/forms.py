from django import forms
from Accounts import models
from django.contrib.auth.models import User
class feedbackForm(forms.ModelForm):
	class Meta:
		model = models.FeedbackProfile
		fields = ['Feedback','Rating']