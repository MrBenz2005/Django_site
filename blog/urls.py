from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import url


urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/', include('allauth.urls')),
]
