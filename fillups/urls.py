from django.urls import path, reverse
from fillups import views

app_name = 'fillups'

urlpatterns = [
    path('myprofile/',views.UserProfile.as_view(),name='user_profile'),
    path('myprofile/fillups/',views.UserFillupListView.as_view(),name='user_fillup_list'),
    path('myprofile/cars/',views.UserCarListView.as_view(),name='user_car_list'),
    path('myprofile/stats/',views.UserStatsView.as_view(),name='user_stats'),
    path('all/fillups/',views.AllFillupListView.as_view(),name='all_fillup_list'),
    path('all/cars/',views.AllCarListView.as_view(),name='all_car_list'),
    path('new/fillup',views.NewFillup.as_view(success_url='/myprofile/fillups/'),name='new_fillup'),
    path('myprofile/fillups/edit/<int:pk>/',views.UpdateFillup.as_view(success_url='/myprofile/fillups/'),name='update_fillup'),
    path('myprofile/fillups/delete/<int:pk>/',views.FillupDeleteView.as_view(),name='delete_fillup'),
    path('myprofile/cars/edit/<int:pk>',views.UpdateCar.as_view(success_url='/myprofile/cars/'),name='update_car'),
    path('myprofile/cars/delete/<int:pk>',views.CarDeleteView.as_view(),name='delete_car'),
    path('new/car',views.NewCar.as_view(success_url='/myprofile/cars/'),name='new_car'),
]
