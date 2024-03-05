from django.urls import path
from envdata import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('nav_forms',views.NavForms.as_view(),name='nav_forms'),
    path('companies', views.CompanyListView.as_view(), name='companies_list'),
    path('company/<uuid:pk>/', views.CompanyDetailView.as_view(), name='single_company'),
    path('create-company/', views.CompanyCreateView.as_view(), name='create_company'),
    path('update-company/<uuid:pk>/', views.CompanyUpdateView.as_view(), name='update_company'),
    path('delete-company/<uuid:pk>/', views.CompanyDeleteView.as_view(), name='delete_company'),

    path('fuel-emissions/', views.FuelListView.as_view(), name='fuel_emissions'),
    path('fuel-emission/<uuid:pk>/', views.FuelDetailView.as_view(), name='fuel_emission'),
    path('create-fuel-emission/', views.FuelCreateView.as_view(), name='create_fuel_emission'),
    path('update-fuel-emission/<uuid:pk>/', views.FuelUpdateView.as_view(), name='update_fuel_emission'),
    path('delete-fuel-emission/<uuid:pk>/', views.FuelDeleteView.as_view(), name='delete_fuel_emission'),

    path('sf6-emissions/', views.Sf6ListView.as_view(), name='sf6_emissions'),
    path('sf6-emission/<uuid:pk>/', views.Sf6DetailView.as_view(), name='sf6_emission'),
    path('create-sf6-emissions/', views.Sf6CreateView.as_view(), name='create_sf6_emissions'),
    path('update-sf6-emission/<uuid:pk>/', views.Sf6UpdateView.as_view(), name='update_sf6_emissions'),
    path('delete-sf6-emission/<uuid:pk>/', views.Sf6DeleteView.as_view(), name='delete_sf6_emissions'),

    path('refrigerant-emissions/', views.RefrigerantView.as_view(), name='refrigerant_emissions'),
    path('refrigerant-emission/<uuid:pk>/', views.RefrigerantDetailView.as_view(),
         name='refrigerant_emission'),
    path('create-refrigerant-emissions/', views.RefrigerantCreateView.as_view(),
         name='create_refrigerant_emissions'),
    path('update-refrigerant-emission/<uuid:pk>/', views.RefrigerantUpdateView.as_view(),
         name='update_refrigerant_emissions'),
    path('delete-refrigerant-emission/<uuid:pk>/', views.RefrigerantDeleteView.as_view(),
         name='delete_refrigerant_emissions'),

    path('energy-aq-emissions/', views.EnergyListView.as_view(), name='energy_acquisitions'),
    path('energy-aq-emission/<uuid:pk>/', views.EnergyDetailView.as_view(), name='energy_acquisition'),
    path('create-energy-ag-emissions/', views.EnergyCreateView.as_view(), name='create_energy_eq_emissions'),
    path('update-energy-emission/<uuid:pk>/', views.EnergyUpdateView.as_view(),
         name='update_energy_aq_emissions'),
    path('delete-energy-eq-emission/<uuid:pk>/', views.EnergyDeleteView.as_view(),
         name='delete_energy_eq_emissions'),

    path('travels/', views.TravelListView.as_view(), name='travels'),
    path('travel/<uuid:pk>/', views.TravelDetailView.as_view(), name='travel'),
    path('create-travel/', views.TravelCreateView.as_view(), name='create_travel'),
    path('update-travel/<uuid:pk>/', views.TravelUpdateView.as_view(), name='update_travel'),
    path('delete-travel/<uuid:pk>/', views.TravelDeleteView.as_view(), name='delete_travel'),

    path('wastes/', views.WasteListView.as_view(), name='wastes'),
    path('waste/<uuid:pk>/', views.WasteDetailView.as_view(), name='waste'),
    path('create-waste/', views.WasteCreateView.as_view(), name='create_waste'),
    path('update-waste/<uuid:pk>/', views.WasteUpdateView.as_view(), name='update_waste'),
    path('delete-waste/<uuid:pk>/', views.WasteDeleteView.as_view(), name='delete_waste'),

]
