from django.urls import path
from envdata import views

urlpatterns = [

    path('', views.CompanyListView.as_view, name='companies_list'),
    path('company/<uuid:pk>/', views.CompanyDetailView.as_view, name='company'),
    path('create-company/', views.CompanyCreateView.as_view, name='create_company'),
    path('update-company/<uuid:pk>/', views.CompanyUpdateView.as_view, name='update_company'),
    path('delete-company/<uuid:pk>/', views.CompanyDeleteView.as_view, name='delete_company'),

    path('fuel-emissions/', views.FuelListView.as_view(), name='fuel_emissions'),
    path('fuel-emission/<uuid:pk>/', views.FuelDetailView.as_view(), name='fuel_emission'),
    path('create-fuel-emission/', views.FuelCreateView.as_view(), name='create_fuel_emission'),
    path('update-fuel-emission/<uuid:pk>/', views.FuelUpdateView.as_view(), name='update_fuel_emission'),
    path('delete-fuel-emission/<uuid:pk>/', views.FuelDeleteView.as_view(), name='delete_fuel_emission'),

    path('sf6-emissions/', views.Sf6EmissionListView.as_view(), name='sf6_emissions'),
    path('sf6-emission/<uuid:pk>/', views.Sf6EmissionDetailView.as_view(), name='sf6_emission'),
    path('create-sf6-emissions/', views.Sf6EmissionCreateView.as_view(), name='create_sf6_emissions'),
    path('update-sf6-emission/<uuid:pk>/', views.Sf6EmissionUpdateView.as_view(), name='update_sf6_emissions'),
    path('delete-sf6-emission/<uuid:pk>/', views.Sf6EmissionDeleteView.as_view(), name='delete_sf6_emissions'),

    path('refrigerant-emissions/', views.RefrigerantsEmissionsView.as_view(), name='refrigerant_emissions'),
    path('refrigerant-emission/<uuid:pk>/', views.RefrigerantsEmissionsDetailView.as_view(),
         name='refrigerant_emission'),
    path('create-refrigerant-emissions/', views.RefrigerantsEmissionsCreateView.as_view(),
         name='create_refrigerant_emissions'),
    path('update-refrigerant-emission/<uuid:pk>/', views.RefrigerantsEmissionsUpdateView.as_view(),
         name='update_refrigerant_emissions'),
    path('delete-refrigerant-emission/<uuid:pk>/', views.RefrigerantsEmissionsDeleteView.as_view(),
         name='delete_refrigerant_emissions'),

    path('energy-aq-emissions/', views.EnergyListView.as_view(), name='energy__aq_emissions'),
    path('energy-aq-emission/<uuid:pk>/', views.EnergyDetailView.as_view(), name='energy_aq__emission'),
    path('create-energy-ag-emissions/', views.EnergyCreateView.as_view(), name='create_energy_eq_emissions'),
    path('update-energy-emission/<uuid:pk>/', views.EnergyUpdateView.as_view(),
         name='update_energy_aq_emissions'),
    path('delete-energy-eq-emission/<uuid:pk>/', views.EnergyDeleteView.as_view(),
         name='delete_energy_eq_emissions'),

    path('distances/', views.TravelEmissionsListView.as_view(), name='distances'),
    path('distance/<uuid:pk>/', views.TravelEmissionsDetailView.as_view(), name='distance'),
    path('create-distance/', views.TravelEmissionsCreateView.as_view(), name='create_distance'),
    path('update-distance/<uuid:pk>/', views.TravelEmissionsUpdateView.as_view(), name='update_distance'),
    path('delete-distance/<uuid:pk>/', views.TravelDeleteView.as_view(), name='delete_distance'),
]
