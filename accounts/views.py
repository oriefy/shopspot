from django.shortcuts import render
from django.views.generic import CreateView
from accounts.models import User
from accounts.forms import BuyerSignUpForm, SellerSignUpForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('explorer:home')

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('explorer:home')
