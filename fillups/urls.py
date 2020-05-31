from django.urls import path
from fillups import views

urlpatterns = [
    path('fillups/',views.FillupListView.as_view(),name='fillup_list'),
]
