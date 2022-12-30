from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import CharField, Value
from main.models import Ticket, Review


def home(request):
    return render(request, 'main/home.html')


def subscribs(request):
    return render(request, 'main/subscribs.html')


def contributions(request):
    tickets = Ticket.objects.filter(user__username = 'ludovicsansone')
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user__username = 'ludovicsansone')
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    context = sorted(
        chain(reviews, tickets), 
        key=lambda context: context.time_created, 
        reverse=True
    )

    return render(request, 'main/contributions.html', {'context': context})
        

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