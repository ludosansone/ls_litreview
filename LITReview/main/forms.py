from django import forms
from main.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class FollowForm(forms.Form):
    username = forms.fields.CharField(max_length=50, label="Nom d'utilisateur")
