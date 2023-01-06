from itertools import chain
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import CharField, Value
from main.models import Ticket, Review, UserFollows, User
from main.forms import TicketForm, ReviewForm, FollowForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def home(request):
    return render(request, 'main/home.html')


@login_required
def subscribs(request):
    if request.method == 'POST':
        form = FollowForm(request.POST)
        if form.is_valid():
            try:
                followed_user = User.objects.get(username=form.cleaned_data['username'])
                if request.user == followed_user:
                    messages.add_message(request, messages.ERROR, 'Attention ! Vous ne pouvez pas vous suivre vous même.')
                    return redirect('subscribs')
                else:
                    user_follows = UserFollows(
                        user=request.user,
                        followed_user=followed_user)
                    user_follows.save()
                    return redirect('subscribs')
            except:
                messages.add_message(request, messages.ERROR, "Attention ! cet utilisateur n'existe pas.")
                return redirect('subscribs')
    else:
        form = FollowForm()
        followed_users = UserFollows.objects.filter(user=request.user)
        users = UserFollows.objects.filter(followed_user=request.user)
    return render(request, 'main/subscribs.html', {
        'form': form,
        'followed_users': followed_users,
        'users': users})


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
            ticket = Ticket(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                user=request.user)
            ticket.save()
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
            review = Review(
                headline=form.cleaned_data['headline'],
                body=form.cleaned_data['body'],
                rating=form.cleaned_data['rating'],
                user=request.user,
                ticket=review_ticket)
            review.save()
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


@login_required
def new_ticket_and_review(request):
    if request.method == 'POST':
        form_ticket = TicketForm(request.POST)
        form_review = ReviewForm(request.POST)
        if (form_ticket.is_valid()) and (form_review.is_valid()):
            new_ticket = Ticket(
                title=form_ticket.cleaned_data['title'],
                description=form_ticket.cleaned_data['description'],
                user=request.user)
            new_ticket.save()
            new_review = Review(
                ticket=new_ticket,
                user=request.user,
                headline=form_review.cleaned_data['headline'],
                body=form_review.cleaned_data['body'],
                rating=form_review.cleaned_data['rating'])
            new_review.save()
            return redirect('contributions')
    else:
        form_ticket = TicketForm()
        form_review = ReviewForm()

    return render(request, 'main/new-ticket-and-review.html', {'form_ticket': form_ticket, 'form_review': form_review})


@login_required
def stop_follow(request, id):
    user_to_delete = UserFollows.objects.get(followed_user__id=id, user=request.user)
    user_to_delete.delete()
    return redirect('subscribs')

