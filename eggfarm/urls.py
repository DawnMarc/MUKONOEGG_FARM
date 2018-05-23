from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from eggfarm import views
from eggfarm.views import LoginUserView, HomeView, HistoryView     # InvoiceView  # DashboardView, # RegisterUserView,

urlpatterns = [
    url(r'^register', views.signup, name='register'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^book', views.booking, name='book'),
    # url(r'^logout', views.LogoutView.as_view(), name='logout'),
    url(r'^prev_order', views.HistoryView, name='prev_order.html'),
    url(r'^home', views.HomeView.as_view(), name='home.html'),
    url(r'^invoice', views.invoice, name='invoice'),
    # url(r'^about', views.AboutView.as_view(), name='about'),
    ]