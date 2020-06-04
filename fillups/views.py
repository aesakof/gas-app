from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from fillups.models import Fillup, Car
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class FillupListView(ListView):
    model = Fillup

class CarListView(ListView):
    model = Car

class NewFillup(LoginRequiredMixin,CreateView):
    model = Fillup
    fields = ('date', 'price_per_gallon', 'trip_distance', 'gallons', 'total_sale', 'car')
    redirect_field_name = 'fillup_list'

class NewCar(LoginRequiredMixin,CreateView):
    model = Car
    fields = ('name', 'make', 'model', 'model_year', 'status')
    redirect_field_name = 'car_list'
