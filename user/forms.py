from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.models import User
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('A user with that email already exists.')
        return email
