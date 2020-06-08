from django.urls import path, reverse
from fillups import views

app_name = 'fillups'

urlpatterns = [
    path('myprofile/fillups/',views.UserFillupListView.as_view(),name='user_fillup_list'),
    path('myprofile/cars/',views.UserCarListView.as_view(),name='user_car_list'),
    path('all/fillups/',views.AllFillupListView.as_view(),name='all_fillup_list'),
    path('all/cars/',views.AllCarListView.as_view(),name='all_car_list'),
    path('new/fillup',views.NewFillup.as_view(success_url='/myprofile/fillups/'),name='new_fillup'),
    path('myprofile/fillups/<int:pk>/',views.UpdateFillup.as_view(success_url='/myprofile/fillups/'),name='update_fillup'),
    path('myprofile/cars/<int:pk>',views.UpdateCar.as_view(success_url='/myprofile/cars/'),name='update_car'),
    path('new/car',views.NewCar.as_view(success_url='/myprofile/cars/'),name='new_car'),
]
