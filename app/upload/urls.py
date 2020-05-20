from django.urls import path

from . import views

urlpatterns = [
        path('', views.uploadfiles, name='uploadfiles'),
        ]
        
