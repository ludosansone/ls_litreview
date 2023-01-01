from itertools import chain
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import CharField, Value
from main.models import Ticket, Review
from main.forms import TicketForm, ReviewForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'main/home.html')


@login_required
def subscribs(request):
    return render(request, 'main/subscribs.html')


@login_required
def contributions(request):
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    context = sorted(
        chain(reviews, tickets),
        key=lambda context: context.time_created,
        reverse=True
    )

    return render(request, 'main/contributions.html', {'context': context})


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = TicketForm()

    return render(request, 'main/new-ticket.html', {'form': form})


@login_required
def edit_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'main/edit-ticket.html', {'form': form, 'ticket': ticket})


@login_required
def new_review(request, ticket_id):
    review_ticket = Ticket .objects.get(id=ticket_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = Review(
                headline=form.cleaned_data['headline'],
                body=form.cleaned_data['body'],
                rating=form.cleaned_data['rating'],
                user=form.cleaned_data['user'],
                ticket=review_ticket)
            new_review.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'main/new-review.html', {'form': form})


@login_required
def edit_review(request, id):
    review = Review.objects.get(id=id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'main/edit-review.html', {'form': form, 'review': review})


@login_required
def details_ticket(request, id):
    ticket = Ticket.objects.get(id=id)

    return render(request, 'main/details-ticket.html', {'ticket': ticket})


@login_required
def details_review(request, id):
    review = Review.objects.get(id=id)

    return render(request, 'main/details-review.html', {'review': review})


@login_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)

    if request.method == 'POST':
        ticket.delete()
        return redirect('contributions')

    return render(request, 'main/delete-ticket.html', {'ticket': ticket})


@login_required
def delete_review(request, id):
    review = Review.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('contributions')

    return render(request, 'main/delete-review.html', {'review': review})
