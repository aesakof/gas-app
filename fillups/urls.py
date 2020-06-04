from django.urls import path, reverse
from fillups import views

app_name = 'fillups'

urlpatterns = [
    path('fillups/',views.FillupListView.as_view(),name='fillup_list'),
    path('cars/',views.CarListView.as_view(),name='car_list'),
    path('new/fillup',views.NewFillup.as_view(success_url='/fillups/'),name='new_fillup'),
    path('new/car',views.NewCar.as_view(success_url='/cars/'),name='new_car'),
]
