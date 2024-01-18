from django.urls import path
from envdata import views

urlpatterns = [path('', views.EmissionListView.as_view(), name='emissions'),
               path('emission/<uuid:pk>/', views.EmissionDetailView.as_view(), name='emission'),
               path('create-emission/', views.EmissionCreateView.as_view(), name='create_emission'),
               path('update-emission/<uuid:pk>/', views.EmissionUpdateView.as_view(), name='update_emission'),
               path('delete-emission/<uuid:pk>/', views.delete_emission, name='delete_emission'),

               path('fuel-emissions/', views.fuel_emissions, name='fuel_emissions'),
               path('fuel-emission/<uuid:pk>/', views.fuel_emission, name='fuel_emission'),
               path('create-fuel-emission/', views.create_fuel_emission, name='create_fuel_emission'),
               path('update-fuel-emission/<uuid:pk>/', views.update_fuel_emission, name='update_fuel_emission'),
               path('delete-fuel-emission/<uuid:pk>/', views.delete_fuel_emission, name='delete_fuel_emission'),


               path('sf6-emissions/', views.sf6_emissions, name='sf6_emissions'),
               path('sf6-emission/<uuid:pk>/', views.sf6_emission, name='sf6_emission'),
               path('create-sf6-emissions/', views.create_sf6_emission, name='create_sf6_emissions'),
               path('update-sf6-emission/<uuid:pk>/', views.update_sf6_emission, name='update_sf6_emissions'),
               path('delete-sf6-emission/<uuid:pk>/', views.delete_sf6_emission, name='delete_sf6_emissions'),

               path('refrigerant-emissions/', views.refrigerants_emissions, name='refrigerant_emissions'),
               path('refrigerant-emission/<uuid:pk>/', views.refrigerants_emission, name='refrigerant_emission'),
               path('create-refrigerant-emissions/', views.create_refrigerants_emission,name='create_refrigerant_emissions'),
               path('update-refrigerant-emission/<uuid:pk>/', views.update_refrigerants_emission,name='update_refrigerant_emissions'),
               path('delete-refrigerant-emission/<uuid:pk>/', views.delete_refrigerants_emission,name='delete_refrigerant_emissions'),

               path('energy-aq-emissions/', views.energy_acquisitions, name='energy__aq_emissions'),
               path('energy-aq-emission/<uuid:pk>/', views.energy_acquisition, name='energy_aq__emission'),
               path('create-energy-ag-emissions/', views.create_energy_acquisition,name='create_energy_eq_emissions'),
               path('update-energy-emission/<uuid:pk>/', views.update_energy_acquisition,name='update_energy_aq_emissions'),
               path('delete-energy-eq-emission/<uuid:pk>/', views.delete_energy_acquisition,name='delete_energy_eq_emissions'),

               path('distances/', views.distances, name='distances'),
               path('distance/<uuid:pk>/', views.distance, name='distance'),
               path('create-distance/',views.create_distance, name='create_distance'),
               path('update-distance/<uuid:pk>/', views.update_distance, name='update_distance'),
               path('delete-distance/<uuid:pk>/', views.delete_distance, name='delete_distance'),
               ]
