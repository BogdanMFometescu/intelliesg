from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [path('login/', views.CustomLoginView.as_view(), name='login'),
               path('register/', views.RegisterView.as_view(), name='register'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('profiles/', views.ProfileListView.as_view(), name='profiles'),
               path('profile/<uuid:pk>/', views.ProfileDetailView.as_view(), name='profile'),
               path('create-profile/', views.ProfileCreateView.as_view(), name='create_profile'),
               path('update-profile/<uuid:pk>/', views.ProfileUpdateView.as_view(), name='update_profile'),
               path('delete-profile/<uuid:pk>/', views.ProfileDeleteView.as_view(), name='delete_profile'),
               path('account/', views.Account.as_view(), name='account'), ]
