"""tiggolino URL Configuration

We will include an seperate documentation for this project, that you can access via google drive
"""
from django.urls import path
from . import views


app_name='pages'
urlpatterns = [
    path('prices/', views.prices, name='prices'),
    path('events/', views.events, name='events'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('gastro/', views.gastro, name='gastro'),
    path('contact/', views.contact, name='contact'),


    path('', views.home, name='home'),
]


