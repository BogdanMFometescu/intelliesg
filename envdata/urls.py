from django.urls import path
from envdata import views

urlpatterns = [

    path('fuel-emissions/', views.FuelListView.as_view(), name='fuel_emissions'),
    path('fuel-emission/<uuid:pk>/', views.FuelDetailView.as_view(), name='fuel_emission'),
    path('create-fuel-emission/', views.FuelCreateView.as_view(), name='create_fuel_emission'),
    path('update-fuel-emission/<uuid:pk>/', views.FuelUpdateView.as_view(), name='update_fuel_emission'),
    path('delete-fuel-emission/<uuid:pk>/', views.FuelDeleteView.as_view(), name='delete_fuel_emission'),

    path('gas-emissions/', views.NaturalGasListView.as_view(), name='gas_emissions'),
    path('gas-emission/<uuid:pk>/', views.NaturalGasDetailView.as_view(), name='gas_emission'),
    path('create-gas-emission/', views.NaturalGasCreateView.as_view(), name='create_gas_emission'),
    path('update-natural-gas-emission/<uuid:pk>/', views.NaturalGasUpdateView.as_view(), name='update_gas_emission'),
    path('delete-natural-gas-emission/<uuid:pk>/', views.NaturalGasDeleteView.as_view(), name='delete_gas_emission'),

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

    path('targets/', views.TargetListView.as_view(), name='targets'),
    path('target/<uuid:pk>/', views.TargetDetailView.as_view(), name='target'),
    path('create-target/', views.TargetCreateView.as_view(), name='create_target'),
    path('update-target/<uuid:pk>/', views.TargetUpdateView.as_view(), name='update_target'),
    path('delete-target/<uuid:pk>/', views.TargetDeleteView.as_view(), name='delete_target'),

    path('fuel-emission-chart/', views.FuelEmissionsView.as_view(), name='fuel_chart'),
    path('sf6-emission-chart/', views.Sf6EmissionsView.as_view(), name='sf6_chart'),
    path('refrigerant-emission-chart/', views.RefrigerantEmissionsView.as_view(), name='refrigerant_chart'),
    path('energy-emission-chart/', views.EnergyEmissionsView.as_view(), name='energy_chart'),
    path('travel-emission-chart/', views.TravelEmissionsView.as_view(), name='travel_chart'),
    path('waste-emission-chart/', views.WasteEmissionsView.as_view(), name='waste_chart'),
    path('gas-emission-chart', views.NaturalGasEmissionsView.as_view(), name='gas_emission_chart'),

    path('charts', views.Charts.as_view(), name='charts'),
    path('fuel-pdf-report', views.FuelExportPdfView.as_view(), name='fuel_report'),
    path('sf6-pdf-report', views.Sf6ExportPdfView.as_view(), name='sf6_report'),
    path('refrigerant-pdf-report', views.RefrigerantPdfView.as_view(), name='refrigerant_report'),
    path('gas-pdf-report', views.NaturalGasPdfView.as_view(), name='gas_report'),
    path('energy-pdf-report', views.EnergyPdfView.as_view(), name='energy_report'),
    path('waste-pdf-report', views.WastePdfView.as_view(), name='waste_report'),
    path('travel-pdf-report', views.TravelPdfView.as_view(), name='travel_report'),
    path('turnover-pdf-report', views.TaxonomyTurnoverPdfView.as_view(), name='turnover_report'),
    path('opex-pdf-report', views.TaxonomyOpExPdfView.as_view(), name='opex_report'),
    path('capex-pdf-report', views.TaxonomyCapExPdfView.as_view(), name='capex_report'),

    path('upload-fuel-data', views.ExcelUploadView.as_view(), name='upload_fuel_data'),
    path('upload-ng-data', views.ExcelUploadViewForNaturalGas.as_view(), name='upload_ng_data'),
    path('upload-energy-data', views.ExcelUploadViewForEnergy.as_view(), name='upload_energy_data'),
    path('upload-sf6-data', views.ExcelUploadViewForSf6.as_view(), name='upload_sf6_data'),
    path('upload-refrigerant-data', views.ExcelUploadViewForRefrigerant.as_view(), name='upload_refrigerant_data'),
    path('upload-travels-data', views.ExcelUploadViewForTravel.as_view(), name='upload_travel_data'),
    path('upload-waste-data', views.ExcelUploadViewForWaste.as_view(), name='upload_waste_data'),

    path('nav-forms-company', views.NavFormsCompany.as_view(), name='nav_forms_company'),
    path('nav-forms-targets', views.NavFormsTargets.as_view(), name='nav_forms_targets'),
    path('nav-forms-emissions', views.NavFormsEmissions.as_view(), name='nav_forms_emissions'),
    path('nav-forms-taxonomy', views.NavFormsTaxonomy.as_view(), name='nav_forms_taxonomy'),

    path('sectors/', views.TaxonomySectorListView.as_view(), name='sectors'),
    path('sector/<uuid:pk>/', views.TaxonomySectorDetailView.as_view(), name='sector'),
    path('create-sector/', views.TaxonomySectorCreateView.as_view(), name='create_sector'),
    path('update-sector/<uuid:pk>/', views.TaxonomySectorUpdateView.as_view(), name='update_sector'),
    path('delete-sector/<uuid:pk>/', views.TaxonomySectorDeleteView.as_view(), name='delete_sector'),

    path('turnovers/', views.TaxonomyTurnoverListView.as_view(), name='turnovers'),
    path('turnover/<uuid:pk>/', views.TaxonomyTurnoverDetailView.as_view(), name='turnover'),
    path('create-turnover/', views.TaxonomyTurnoverCreateView.as_view(), name='create_turnover'),
    path('update-turnover/<uuid:pk>/', views.TaxonomyTurnoverUpdateView.as_view(), name='update_turnover'),
    path('delete-turnover/<uuid:pk>/', views.TaxonomyTurnoverDeleteView.as_view(), name='delete_turnover'),

    path('all-capex/', views.TaxonomyCapexListView.as_view(), name='capexs'),
    path('capex/<uuid:pk>/', views.TaxonomyCapexDetailView.as_view(), name='capex'),
    path('create-capex/', views.TaxonomyCapexCreateView.as_view(), name='create_capex'),
    path('update-capex/<uuid:pk>/', views.TaxonomyCapexUpdateView.as_view(), name='update_capex'),
    path('delete-capex/<uuid:pk>/', views.TaxonomyCapexDeleteView.as_view(), name='delete_capex'),

    path('opexs/', views.TaxonomyOpexListView.as_view(), name='opexs'),
    path('opex/<uuid:pk>/', views.TaxonomyOpexDetailView.as_view(), name='opex'),
    path('create-opex/', views.TaxonomyOpexCreateView.as_view(), name='create_opex'),
    path('update-opex/<uuid:pk>/', views.TaxonomyOpexUpdateView.as_view(), name='update_opex'),
    path('delete-opex/<uuid:pk>/', views.TaxonomyOpexDeleteView.as_view(), name='delete_opex'),




    

]
