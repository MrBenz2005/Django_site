from django.urls import path
from . import views

urlpatterns = [
    path('', views.picture, name='picture'),
    path('choose_capture', views.capture, name='choose_capture'),
]