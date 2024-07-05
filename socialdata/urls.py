from django.urls import path
from socialdata import views

urlpatterns = [path('hss/', views.HealthAndSafetyListView.as_view(), name='hss'),
               path('hs/<uuid:pk>/', views.HealthAndSafetyDetailView.as_view(), name='hs'),
               path('create-hs/', views.HealthAndSafetyCreateView.as_view(), name='create_hs'),
               path('update-hs/<uuid:pk>/', views.HealthAndSafetyUpdateView.as_view(), name='update_hs'),
               path('delete-hs/<uuid:pk>/', views.HealthAndSafetyDeleteView.as_view(), name='delete_hs'),
               path('soc-nav-forms/', views.NavFormsHealthAndSafety.as_view(), name='soc_form_hs'),
               path('soc-employee-nav-forms/', views.NavFormsEmployees.as_view(), name='soc_form_employees'),

               path('soc-export-to-pdf/', views.HealthAndSafetyPdfView.as_view(), name='soc_export_pdf'),

               path('contracts/', views.EmployeeByContractsListView.as_view(), name='contracts'),
               path('contract/<uuid:pk>/', views.EmployeeByContractsDetailView.as_view(), name='contract'),
               path('create-contract/', views.EmployeeByContractsCreateView.as_view(), name='create_contract'),
               path('update-contract/<uuid:pk>/', views.EmployeeByContractsUpdateView.as_view(),
                    name='update_contract'),
               path('delete-contract/<uuid:pk>/', views.EmployeeByContractsDeleteView.as_view(),
                    name='delete_contract'),

               path('employees/', views.NewEmployeeByAgeListView.as_view(), name='employees'),
               path('employee/<uuid:pk>/', views.NewEmployeeByAgeDetailView.as_view(), name='employee'),
               path('create-employee/', views.NewEmployeeByAgeCreateView.as_view(), name='create_employee'),
               path('update-employee/<uuid:pk>/', views.NewEmployeeByAgeUpdateView.as_view(),
                    name='update_employee'),
               path('delete-employee/<uuid:pk>/', views.NewEmployeeByAgeDeleteView.as_view(),
                    name='delete_employee'),

               path('rotations/', views.RotationRateOfEmployeeByAgeListView.as_view(), name='rotations'),
               path('rotation/<uuid:pk>/', views.RotationRateOfEmployeeByAgeDetailView.as_view(), name='rotation'),
               path('create-rotation/', views.RotationRateOfEmployeeByAgeCreateView.as_view(), name='create_rotation'),
               path('update-rotation/<uuid:pk>/', views.RotationRateOfEmployeeByAgeUpdateView.as_view(),
                    name='update_rotation'),
               path('delete-rotation/<uuid:pk>/', views.RotationRateOfEmployeeByAgeDeleteView.as_view(),
                    name='delete_rotation'),

               path('contracts/', views.EmployeeByContractsListView.as_view(), name='contracts'),
               path('contract/<uuid:pk>/', views.EmployeeByContractsDetailView.as_view(), name='contract'),
               path('create-contract/', views.EmployeeByContractsCreateView.as_view(), name='create_contract'),
               path('update-contract/<uuid:pk>/', views.EmployeeByContractsUpdateView.as_view(),
                    name='update_contract'),
               path('delete-contract/<uuid:pk>/', views.EmployeeByContractsDeleteView.as_view(),
                    name='delete_contract'),

               path('retirements/', views.RetirementRateListView.as_view(), name='retirements'),
               path('retirement/<uuid:pk>/', views.RetirementRateDetailView.as_view(), name='retirement'),
               path('create-retirement/', views.RetirementRateCreateView.as_view(), name='create_retirement'),
               path('update-retirement/<uuid:pk>/', views.RetirementRateUpdateView.as_view(),
                    name='update_retirement'),
               path('delete-retirement/<uuid:pk>/', views.RetirementRateDeleteView.as_view(),
                    name='delete_retirement'),

               ]
