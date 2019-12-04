from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),               # this is for the function-based view.
    path('consecutive/', views.consect, name='home'),               # this is for the function-based view.
    path('trail/', views.trail, name='trail'),               # this is for the function-based view.
    path('resp/', views.prod, name='prod'),
    path('sec/', views.sec, name='sec')
]