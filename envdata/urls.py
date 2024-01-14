from django.urls import path
from envdata import views

urlpatterns = [path('', views.emissions, name='emissions'),
               path('emission/<uuid:pk>/', views.emission, name='emission'),
               path('create-emission/', views.create_emission, name='create_emission'),
               path('fuel-emissions/', views.fuel_emissions, name='fuel_emissions'),
               path('fuel-emission/<uuid:pk>/', views.fuel_emission, name='fuel_emission'),
               path('create-fuel-emission/', views.create_fuel_emission, name='create_fuel_emission')
               ]
