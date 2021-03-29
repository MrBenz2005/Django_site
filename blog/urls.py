from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('rating/', views.rating, name='rating'),
    path('accounts/', include('allauth.urls')),
]
