from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreationForm, ContactForm


class SignUp(CreateView):
    """
    Registration form
    """
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ContactView(CreateView):
    """
    Сontact form with admin
    """
    form_class = ContactForm
    success_url = reverse_lazy('posts:index')
    template_name = 'contact_form.html'

