from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from fillups.models import Fillup, Car
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

# Create your views here.
class UserFillupListView(ListView):
    template_name = 'fillups/user_fillup_list.html'
    model = Fillup
    context_object_name = 'user_fillup_list'
    ordering = ['-date']

    def get_queryset(self):
        return Fillup.objects.filter(username=self.request.user).order_by('-date')

class AllFillupListView(ListView):
    template_name = 'fillups/all_fillup_list.html'
    model = Fillup
    context_object_name = 'all_fillup_list'
    ordering = ['-date']

class UserCarListView(ListView):
    template_name = 'fillups/user_car_list.html'
    model = Car
    context_object_name = 'user_car_list'
    ordering = ['name']

    def get_queryset(self):
        return Car.objects.filter(username=self.request.user).order_by('name')

class AllCarListView(ListView):
    template_name = 'fillups/all_car_list.html'
    model = Car
    context_object_name = 'all_car_list'
    ordering = ['name']

class NewFillup(LoginRequiredMixin,CreateView):
    model = Fillup
    form_class = forms.FillupForm
    redirect_field_name = 'fillups:fillup_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class UpdateFillup(LoginRequiredMixin,UpdateView):
    model = Fillup
    form_class = forms.FillupForm
    redirect_field_name = 'fillups:fillup_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class FillupDeleteView(LoginRequiredMixin,DeleteView):
    model = Fillup
    success_url = reverse_lazy('fillups:user_fillup_list')

class NewCar(LoginRequiredMixin,CreateView):
    model = Car
    form_class = forms.CarForm
    redirect_field_name = 'fillups:car_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class UpdateCar(LoginRequiredMixin,UpdateView):
    model = Car
    form_class = forms.CarForm
    redirect_field_name = 'fillups:user_car_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class CarDeleteView(LoginRequiredMixin,DeleteView):
    model = Car
    success_url = reverse_lazy('fillups:user_car_list')
