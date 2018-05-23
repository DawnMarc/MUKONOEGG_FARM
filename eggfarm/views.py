# Create your views here.

from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, TemplateView, ListView
from .models import Orders
from .forms import ClientRegistrationForm, LoginForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'general/home.html'


class InvoiceView(generic.TemplateView):
    template_name = 'general/invoice.html'


def invoice(request):
        return Orders.objects.raw('SELECT user, Prices, order_no, no_of_trays, location, request_date, total_amt_due')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'general/invoice.html')
    else:
        form = BookingForm()
    return render(request, 'general/book.html', {'form': form})


class HistoryView(generic.ListView):
    template_name = 'general/prev_order.html'

    def get_queryset(self):
        return Orders.objects.filter(request_date__lte=timezone.now()).order_by('-request_date')


def signup(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            username = authenticate(username=username, password=raw_password)
            login(request, username)
            return render(request, 'general/interlude.html')
    else:
        form = ClientRegistrationForm()

    return render(request, 'general/register.html', {'form': form})


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "registration/../templates/general/login.html"

    def valiadation(self):
        user = authenticate(username=username, password=raw_password)

        if user is not None:
            return HttpResponse("Signed in")

        else:
            return HttpResponse("Not signed in")


