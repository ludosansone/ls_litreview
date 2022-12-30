from itertools import chain
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import CharField, Value
from main.models import Ticket, Review
from main.forms import TicketForm


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
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_title = form.cleaned_data['title']
            ticket_description = form.cleaned_data['description']

            return redirect('home')
    else:
        form = TicketForm()

    return render(request, 'main/new-ticket.html', {'form': form})


def edit_ticket(request, id):
    result = Ticket.objects.get(id = id)

    return render(request, 'main/edit-ticket.html', {'result': result})


def new_review(request):
    return render(request, 'main/new-review.html')


def edit_review(request, id):
    result = Review.objects.get(id = id)

    return render(request, 'main/edit-review.html', {'result': result})
