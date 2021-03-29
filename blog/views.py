from django.shortcuts import render

def main(request):
    return render(request, 'blog/mainPage.html', {})

def rating(request):
    return render(request, 'blog/dummy.html', {})



# Create your views here.
