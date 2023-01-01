from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=42, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
