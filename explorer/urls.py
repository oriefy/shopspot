from django.urls import include, path

from .views import home

urlpatterns = [
    path('', home.home, name='home'),
]
