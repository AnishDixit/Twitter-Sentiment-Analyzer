from django.contrib import admin
from .models import Profile,HashtagProfile,FeedbackProfile
# Register your models here.
admin.site.register(Profile)
admin.site.register(FeedbackProfile)
admin.site.register(HashtagProfile)