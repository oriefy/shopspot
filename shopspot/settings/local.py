from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='^92l&5_l2f-ik5xlav!7*cat904fro-lmdd@0kgz@c*nxua3@p')

DEBUG = env.bool('DJANGO_DEBUG', default=True)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
