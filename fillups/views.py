from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.db.models import Sum, Avg, F, Func
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

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        bunch_of_stats = {
            'total_cars': Car.objects.filter(username=self.request.user).count(),
            'total_fillups': Fillup.objects.filter(username=self.request.user).count(),
            'total_distance': Fillup.objects.filter(username=self.request.user).aggregate(Sum('trip_distance')),
            'total_gallons': Fillup.objects.filter(username=self.request.user).aggregate(total_gallons = Round(Sum('gallons'),4)),
            'avg_price': Fillup.objects.filter(username=self.request.user).aggregate(avg_price = Round(Avg('price_per_gallon'),3)),
            'total_spent': sum_total_sale(Fillup.objects.filter(username=self.request.user)),
            'avg_mpg': avg_mpg(Fillup.objects.filter(username=self.request.user))
        }
        context['stats'] = bunch_of_stats
        context['active_cars'] = Car.objects.filter(status='Active').filter(username=self.request.user)
        context['last_10_fillups'] = Fillup.objects.filter(username=self.request.user).order_by('-date')[:10]
        return context

class UserStatsView(TemplateView):
    template_name = 'fillups/user_stats.html'

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

class UpdateFillup(LoginRequiredMixin,TestUserOfObject,UpdateView):
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

class FillupDeleteView(LoginRequiredMixin,TestUserOfObject,DeleteView):
    model = Fillup
    success_url = reverse_lazy('fillups:user_fillup_list')

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

class NewCar(LoginRequiredMixin,CreateView):
    model = Car
    form_class = forms.CarForm
    redirect_field_name = 'fillups:car_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class UpdateCar(LoginRequiredMixin,TestUserOfObject,UpdateView):
    model = Car
    form_class = forms.CarForm
    redirect_field_name = 'fillups:user_car_list'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class CarDeleteView(LoginRequiredMixin,TestUserOfObject,DeleteView):
    model = Car
    success_url = reverse_lazy('fillups:user_car_list')

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
    for row in queryset:
        mpg_list.append(row.mpg)
    return round(mean(mpg_list),4)
