from django.shortcuts import render


from django.contrib.auth.forms import UserCreationForm
from blog.forms import RegisterForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'