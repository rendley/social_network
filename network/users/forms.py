from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Contact


User = get_user_model()


class CreationForm(UserCreationForm):
    """
    Registration form
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ContactForm(ModelForm):
    """
    Сontact form with admin
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'body']