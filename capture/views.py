from django.shortcuts import render
from django.http import HttpResponse

def capture(request):
	return render(request, 'capture/choose_capture.html', {})

def picture(request):
    return render(request, 'blog/mainPage.html', {})
# Create your views here.
