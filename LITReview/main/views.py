from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')


def subscribs(request):
    return render(request, 'main/subscribs.html')


def contributions(request):
    return render(request, 'main/contributions.html')


def signin(request):
    return render(request, 'main/signin.html')


def signup(request):
    return render(request, 'main/signup.html')


def new_ticket(request):
    return render(request, 'main/new-ticket.html')


def edit_ticket(request):
    return render(request, 'main/edit-ticket.html')


def new_review(request):
    return render(request, 'main/new-review.html')


def edit_review(request):
    return render(request, 'main/edit-review.html')