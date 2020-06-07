from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from fillups.models import Fillup, Car
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

# Create your views here.
class FillupListView(ListView):
    model = Fillup
    context_object_name = 'fillup_list'
    ordering = ['-date']

    def get_queryset(self):
        return Fillup.objects.filter(username=self.request.user)

class CarListView(ListView):
    model = Car
    context_object_name = 'car_list'
    ordering = ['name']

    def get_queryset(self):
        return Car.objects.filter(username=self.request.user)

class NewFillup(LoginRequiredMixin,CreateView):
    model = Fillup
    form_class = forms.FillupForm
    redirect_field_name = 'fillup_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class NewCar(LoginRequiredMixin,CreateView):
    model = Car
    form_class = forms.CarForm
    redirect_field_name = 'car_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
