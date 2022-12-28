from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class meta:
        unique_together = ('user', 'followed_user')
        body = models.TextField(verbose_name='Body',
                                max_length=8192,
                                blank=True)
        time_created = models.DateTimeField(validators='Creation date',
                                            auto_now=True)
