from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser
)

# Create your models here.
class User(AbstractBaseUser):
    email       = models.EmailField(
        _('Email'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Valid email addresses only.'),
        error_messages={
            'unique': _("That email address is already registered."),
        },
    )

    USERNAME_FIELD = 'email'
    