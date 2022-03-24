from re import template
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView

from .forms import UpdateUserForm
from .models import User

class UsersMapView(LoginRequiredMixin,TemplateView):

    template_name = "map.html"

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class UserHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'