
from django.urls import path
from companies import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('quik-start', views.QuickStart.as_view(), name='quick_start'),
    path('companies', views.CompanyListView.as_view(), name='companies_list'),
    path('company/<uuid:pk>/', views.CompanyDetailView.as_view(), name='single_company'),
    path('create-company/', views.CompanyCreateView.as_view(), name='create_company'),
    path('update-company/<uuid:pk>/', views.CompanyUpdateView.as_view(), name='update_company'),
    path('delete-company/<uuid:pk>/', views.CompanyDeleteView.as_view(), name='delete_company'),
]