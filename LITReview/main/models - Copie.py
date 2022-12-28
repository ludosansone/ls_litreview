from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Ticket(models.Model):
    title = models.CharField(verbose_name='Ticket tile', max_length=128)
    description = models.CharField(verbose_name='Ticket description',
                                   max_length=2048,
                                   blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, default=Ticket)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='following')


class User(AbstractUser):
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='Followed_by',
                                      null=True)

    class meta:
        unique_together = ('user', 'followed_user')
        body = models.TextField(verbose_name='Body',
                                max_length=8192,
                                blank=True)
        ticket = models.ForeignKey(to=Ticket,
                                   on_delete=models.CASCADE)
        time_created = models.DateTimeField(validators='Creation date',
                                            auto_now=True)
