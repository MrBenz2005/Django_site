from django.shortcuts import render
from django.http import HttpResponse

def capture(request):
	return render(request, 'blog/choose_capture.html', {})
# Create your views here.
