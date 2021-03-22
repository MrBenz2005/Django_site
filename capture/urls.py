from django.urls import path
from . import views

urlpatterns = [
    path('choose_capture', views.capture, name='choose_capture'),
]