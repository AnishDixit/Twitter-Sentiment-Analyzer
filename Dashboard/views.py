from django.shortcuts import render
from Accounts.models import Profile,HashtagProfile,FeedbackProfile 
from . import forms
# Create your views here.
def home(request):
	tweets = HashtagProfile.objects.all()#get(Username=request.user)
	for tweet in tweets:
		print(tweet.Hashtag_Searched)
	return render(request,'Dashboard/home.html',{'tweets':tweets})

def feedback(request):
	if request.method == "POST":
		form= forms.feedbackForm(request.POST)
		if form.is_valid():
		    instance = form.save(commit=False)
		    print(instance.Feedback)
		    instance.Username = request.user
		    instance.save()
		    feedbacks = FeedbackProfile.objects.all()
		    tweets = HashtagProfile.objects.all()#get(Username=request.user)
		    return render (request,'Dashboard/showFeedback.html',{'feedbacks':feedbacks,'tweets':tweets})
	else:
		form = forms.feedbackForm()
	return render(request,'Dashboard/feedback.html',{'form':form})