from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def home_view(request):
	return render(request, 'homePage.html')