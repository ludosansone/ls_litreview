from django.contrib import admin
from main.models import User, Ticket, Review


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'user')
