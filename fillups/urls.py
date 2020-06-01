from django.urls import path
from fillups import views

app_name = 'fillups'

urlpatterns = [
    path('fillups/',views.FillupListView.as_view(),name='fillup_list'),
    path('cars/',views.CarListView.as_view(),name='car_list'),
]
