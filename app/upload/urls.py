from django.urls import path

from . import views

urlpatterns = [
        path('input', views.uploadfiles, name='uploadfiles'),
        path('output', views.tables, name='tables'),
        ]
        
