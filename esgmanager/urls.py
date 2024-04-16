from django.urls import path
from esgmanager import views

urlpatterns = [path('pillars/', views.ListViewPillars.as_view(), name='pillars'),
               path('pillar/<uuid:pk>/', views.DeleteViewPillars.as_view(), name='pillar'),
               path('create-pillar/', views.CreateViewPillars.as_view(), name='create_pillar'),
               path('update-pillar/<uuid:pk>/', views.UpdateViewPillars.as_view(), name='update_pillar'),
               path('delete-pillar/<uuid:pk>/', views.DeleteViewPillars.as_view(), name='delete_pillar')]
