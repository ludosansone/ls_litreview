from django.shortcuts import render
from django.http import HttpResponse
from main.models import Ticket


def home(request):
    return render(request, 'main/home.html')


def subscribs(request):
    return render(request, 'main/subscribs.html')


def contributions(request):
    results = Ticket.objects.filter(user__username = 'ludovicsansone')

    return render(request, 'main/contributions.html', {'results': results})


def signin(request):
    return render(request, 'main/signin.html')


def signup(request):
    return render(request, 'main/signup.html')


def new_ticket(request):
    return render(request, 'main/new-ticket.html')


def edit_ticket(request, id):
    result = Ticket.objects.get(id = id)
    return render(request, 'main/edit-ticket.html', {'result': result})


def new_review(request):
    return render(request, 'main/new-review.html')


def edit_review(request):
    return render(request, 'main/edit-review.html')