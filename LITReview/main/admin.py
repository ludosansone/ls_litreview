from django.contrib import admin
from main.models import User, Ticket


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

