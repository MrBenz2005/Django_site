from django.shortcuts import render

def main(request):
    return render(request, 'blog/mainPage.html', {})


# Create your views here.
