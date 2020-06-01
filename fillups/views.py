from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from fillups.models import Fillup, Car

# Create your views here.
class FillupListView(ListView):
    model = Fillup

class CarListView(ListView):
    model = Car
