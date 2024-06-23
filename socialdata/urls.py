from django.urls import path
from socialdata import views

urlpatterns = [path('hss/', views.HealthAndSafetyListView.as_view(), name='hss'),
               path('hs/<uuid:pk>/', views.HealthAndSafetyDetailView.as_view(), name='hs'),
               path('create-hs/', views.HealthAndSafetyCreateView.as_view(), name='create_hs'),
               path('update-hs/<uuid:pk>/', views.HealthAndSafetyUpdateView.as_view(), name='update_hs'),
               path('delete-hs/<uuid:pk>/', views.HealthAndSafetyDeleteView.as_view(), name='delete_hs')

               ]
