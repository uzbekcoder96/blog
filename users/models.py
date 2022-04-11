from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

from django.conf import settings
from django.core.mail import send_mail



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('Email address', unique=True)
    token_for_activation = models.CharField(max_length=50, null=True, blank=True)
    
    avatar = models.ImageField(blank=True)
    is_staff = models.BooleanField(default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField('active', default=False,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField('Date joined', default=timezone.now)
    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS = ['email']
    objects = UserManager()


    def email_user(self, subject, message, **kwargs):
        return send_mail(
            subject=subject,
            message=message,
            html_message=kwargs.get('html_message', None),
            recipient_list=[self.email],
            from_email=settings.DEFAULT_FROM_EMAIL,
            fail_silently=kwargs.get('fail_silently', True)
        )