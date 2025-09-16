from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={"placeholder": "Digite seu usuário"})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Digite sua senha"})
    )

    error_messages = {
        "invalid_login": "Usuário ou senha incorretos.", 
    }


class MeuUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={
            "placeholder": "Digite seu nome de usuário",
        })
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Digite sua senha",
        })
    )
    password2 = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirme sua senha",
        })
    )

    error_messages = {
        "password_mismatch": "As senhas devem ser iguais",
        "username_exists": "Este usuário já existe.",
    }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(self.error_messages["username_exists"])
        return username