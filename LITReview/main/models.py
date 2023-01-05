from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class meta:
        body = models.TextField(verbose_name='Body',
                                max_length=8192,
                                blank=True)
        time_created = models.DateTimeField(validators='Creation date',
                                            auto_now=True,
                                            verbose_name='Date d\'inscription')


class Ticket(models.Model):
    title = models.CharField(verbose_name='Titre', max_length=128)
    description = models.CharField(verbose_name='Description',
                                   max_length=2048,
                                   blank=True)
    user = models.ForeignKey(to=get_user_model(),
                             on_delete=models.CASCADE,
                             editable=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_review_number(self):
        review_number = Review.objects.filter(ticket=self).count()
        return str(review_number)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE,
                               default=Ticket,
                               editable=False)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                              verbose_name='Notation')
    headline = models.CharField(max_length=128, verbose_name='Entête')
    body = models.CharField(max_length=8192, blank=True, verbose_name='Critique')
    user = models.ForeignKey(to=get_user_model(),
                             on_delete=models.CASCADE,
                             editable=False)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE)
    followed_user = models.ForeignKey(
        User,
        related_name='followed_user',
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'followed_user')
