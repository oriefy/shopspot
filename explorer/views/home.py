from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'explorer/home.html')
