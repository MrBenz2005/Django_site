from django.shortcuts import render
from django.http import HttpResponse
from captcha.image import ImageCaptcha
from .forms import UserForm
import random
import os

def picture(request):
    return render(request, 'blog/mainPage.html', {})

def capture(request):
	image = ImageCaptcha()

	symbols = ['QWERTYUIOPLKJHGFDSAZXCVBNM1234567890']
	vyvod = ' '
	for i in range(6):
		vyvod += symbols[0][random.randint(0, len(symbols[0]) - 1)]
	print(f'CWD: {os.getcwd()}')

	data = image.generate(vyvod)
	image_path = "captcha1.png"
	image.write(vyvod, f"capture/static/{image_path}")


	return 	render(request, 'capture/choose_capture.html', {'image_path': image_path})


def index(request):
  submitbutton= request.POST.get("submit")

  firstname=''
  lastname=''
  emailvalue=''

  form= UserForm(request.POST or None)
  if form.is_valid():
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")

  context= {'form': form, 'firstname': firstname, 
            'lastname':lastname, 'submitbutton': submitbutton,
            'emailvalue':emailvalue}

  return render(request, 'capture/templates/capture/choose_capture.html', context)