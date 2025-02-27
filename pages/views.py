from django.http import Http404
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def home(request):
    context = {}
    return render(request, 'pages/home.html', context)

def prices(request):
    context = {}
    return render(request, 'pages/prices.html', context)

def events(request):
    context = {}
    return render(request, 'pages/events.html', context)

def aboutus(request):
    context = {}
    return render(request, 'pages/aboutus.html', context)

def gastro(request):
    context = {}
    return render(request, 'pages/gastronomie.html', context)


def contact(request):
    context = {}
    if request.POST:
        form = ContactForm(request)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        else:
            raise Http404
    else:
        form = ContactForm()
        context['form']=form
    return render(request, 'pages/contact.html', context)