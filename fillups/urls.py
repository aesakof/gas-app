from django.urls import path, reverse
from fillups import views

app_name = 'fillups'

urlpatterns = [
    path('profile/<str:username>/',views.UserProfile.as_view(),name='user_profile'),
    path('profile/<str:username>/fillups/',views.UserFillupListView.as_view(),name='user_fillup_list'),
    path('profile/<str:username>/cars/',views.UserCarListView.as_view(),name='user_car_list'),
    path('profile/<str:username>/stats/',views.UserStatsView.as_view(),name='user_stats'),
    path('profile/<str:username>/fillups/edit/<int:pk>/',views.UpdateFillup.as_view(success_url='/profile/<str:username>/fillups/'),name='update_fillup'),
    path('profile/<str:username>/fillups/delete/<int:pk>/',views.FillupDeleteView.as_view(),name='delete_fillup'),
    path('profile/<str:username>/cars/edit/<int:pk>',views.UpdateCar.as_view(success_url='/profile/<str:username>/cars/'),name='update_car'),
    path('profile/<str:username>/cars/delete/<int:pk>',views.CarDeleteView.as_view(),name='delete_car'),
    path('all/fillups/',views.AllFillupListView.as_view(),name='all_fillup_list'),
    path('all/cars/',views.AllCarListView.as_view(),name='all_car_list'),
    path('new/fillup',views.NewFillup.as_view(success_url='/profile/fillups/'),name='new_fillup'),
    path('new/car',views.NewCar.as_view(success_url='/profile/cars/'),name='new_car')
]



    # path('myprofile/',views.UserProfile.as_view(),name='user_profile'),
    # path('myprofile/fillups/',views.UserFillupListView.as_view(),name='user_fillup_list'),
    # path('myprofile/cars/',views.UserCarListView.as_view(),name='user_car_list'),
    # path('myprofile/stats/',views.UserStatsView.as_view(),name='user_stats'),
    # path('myprofile/fillups/edit/<int:pk>/',views.UpdateFillup.as_view(success_url='/myprofile/fillups/'),name='update_fillup'),
    # path('myprofile/fillups/delete/<int:pk>/',views.FillupDeleteView.as_view(),name='delete_fillup'),
    # path('myprofile/cars/edit/<int:pk>',views.UpdateCar.as_view(success_url='/myprofile/cars/'),name='update_car'),
    # path('myprofile/cars/delete/<int:pk>',views.CarDeleteView.as_view(),name='delete_car'),
