from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy, reverse
from django.db.models import Sum, Avg, F, Func
from accounts.models import User
from fillups.models import Fillup, Car
from statistics import mean
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import forms


class TestUserOfObject(UserPassesTestMixin):
    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.username

# Create your views here.
class UserProfile(TemplateView):
    template_name = 'fillups/user_profile.html'
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        usr = get_object_or_404(User, username=kwargs.get("username"))
        overview_stats = {
            'total_cars': Car.objects.filter(username=usr).count(),
            'total_fillups': Fillup.objects.filter(username=usr).count(),
            'total_distance': Fillup.objects.filter(username=usr).aggregate(Sum('trip_distance')),
            'total_gallons': Fillup.objects.filter(username=usr).aggregate(total_gallons = Round(Sum('gallons'),4)),
            'avg_price': Fillup.objects.filter(username=usr).aggregate(avg_price = Round(Avg('price_per_gallon'),3)),
            'total_spent': sum_total_sale(Fillup.objects.filter(username=usr)),
            'avg_mpg': avg_mpg(Fillup.objects.filter(username=usr))
        }
        context['profile_name'] = usr.username
        context['stats'] = overview_stats
        context['active_cars'] = Car.objects.filter(status='Active').filter(username=usr)
        context['last_10_fillups'] = Fillup.objects.filter(username=usr).order_by('-date')[:10]
        return context


class UserStatsView(TemplateView):
    template_name = 'fillups/user_stats.html'

    def get_context_data(self, **kwargs):
        usr = get_object_or_404(User, username=self.kwargs.get("username"))
        context = super(UserStatsView,self).get_context_data(**self.kwargs)
        context['profile_name'] = usr.username
        return context


class UserFillupListView(ListView):
    template_name = 'fillups/user_fillup_list.html'
    model = Fillup
    context_object_name = 'user_fillup_list'
    ordering = ['-date']

    def get_queryset(self):
        usr = get_object_or_404(User, username=self.kwargs.get("username"))
        return Fillup.objects.filter(username=usr).order_by('-date')

    def get_context_data(self):
        usr = get_object_or_404(User, username=self.kwargs.get("username"))
        context = super(UserFillupListView,self).get_context_data(**self.kwargs)
        context['profile_name'] = usr.username
        return context


class AllFillupListView(ListView):
    template_name = 'fillups/all_fillup_list.html'
    model = Fillup
    context_object_name = 'all_fillup_list'
    ordering = ['-date']


class NewFillup(LoginRequiredMixin,CreateView):
    model = Fillup
    form_class = forms.FillupForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('fillups:user_fillup_list', kwargs={'username': self.object.username})


class UpdateFillup(LoginRequiredMixin,TestUserOfObject,UpdateView):
    model = Fillup
    form_class = forms.FillupForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('fillups:user_fillup_list', kwargs={'username': self.object.username})


class FillupDeleteView(LoginRequiredMixin,TestUserOfObject,DeleteView):
    model = Fillup

    def get_success_url(self):
        return reverse('fillups:user_fillup_list', kwargs={'username': self.object.username})


class UserCarListView(ListView):
    template_name = 'fillups/user_car_list.html'
    model = Car
    context_object_name = 'user_car_list'
    ordering = ['name']

    def get_queryset(self):
        usr = get_object_or_404(User, username=self.kwargs.get("username"))
        return Car.objects.filter(username=usr).order_by('name')

    def get_context_data(self):
        usr = get_object_or_404(User, username=self.kwargs.get("username"))
        context = super(UserCarListView,self).get_context_data(**self.kwargs)
        context['profile_name'] = usr.username
        return context


class AllCarListView(ListView):
    template_name = 'fillups/all_car_list.html'
    model = Car
    context_object_name = 'all_car_list'
    ordering = ['name']


class NewCar(LoginRequiredMixin,CreateView):
    model = Car
    form_class = forms.CarForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fillups:user_car_list', kwargs={'username': self.object.username})


class UpdateCar(LoginRequiredMixin,TestUserOfObject,UpdateView):
    model = Car
    form_class = forms.CarForm
    redirect_field_name = 'fillups:user_car_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fillups:user_car_list', kwargs={'username': self.object.username})


class CarDeleteView(LoginRequiredMixin,TestUserOfObject,DeleteView):
    model = Car

    def get_success_url(self):
        return reverse('fillups:user_car_list', kwargs={'username': self.object.username})

###############################################################################

class Round(Func):
  function = 'ROUND'
  arity = 2

def sum_total_sale(queryset):
    total = 0
    for row in queryset:
        total += row.total_sale
    return total

def avg_mpg(queryset):
    mpg_list = []
    if len(queryset) == 0:
        return 0
    else:
        for row in queryset:
            mpg_list.append(row.mpg)
        return round(mean(mpg_list),4)
