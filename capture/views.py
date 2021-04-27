from django.shortcuts import render
from django.http import HttpResponse
from captcha.image import ImageCaptcha
import random

def picture(request):
    return render(request, 'blog/mainPage.html', {})

def capture(request):
	image = ImageCaptcha()

	symbols = ['QWERTYUIOPLKJHGFDSAZXCVBNM1234567890']
	vyvod = ' '
	for i in range(6):
		vyvod += symbols[0][random.randint(0, len(symbols[0]))]

	data = image.generate(vyvod)
	capture_write = image.write(vyvod, 'captcha1.png')
	return 	render(request, 'capture/choose_capture.html', {'vyvod': vyvod})
