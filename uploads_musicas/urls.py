from django.urls import path

from . import views

app_name = 'musicas'

urlpatterns = [
    path('', views.IndexView, name='index')
]