from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('input', views.uploadfiles, name='uploadfiles'),
        path('detail/<slug:companynumber>/', views.detail, name='detail'),
        path('output/<slug:category>', views.tables, name='tables'),
        path('test/', views.test, name='test')
        ]

