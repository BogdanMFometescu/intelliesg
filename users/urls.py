from django.urls import path
from users import views

urlpatterns = [path('login/', views.CustomLoginView.as_view(), name='login'),
               path('register/', views.RegisterView.as_view(), name='register'),
               path('profiles/', views.ProfileListView.as_view(),name='profiles'),
               path('profiles/<uuid:pk>/', views.ProfileListView.as_view(),name='profiles'),
               path('account/', views.Account.as_view(),name='account'),]
