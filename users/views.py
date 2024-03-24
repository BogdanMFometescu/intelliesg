from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from users.models import Profile
from django.views.generic.edit import FormView
from django.contrib.auth import login
from users.forms import ProfileForm, CustomUserCreationForm
from django.views.generic import TemplateView


class Account(LoginRequiredMixin, TemplateView):
    template_name = 'starter.html'


class CustomLoginView(LoginView):
    template_name = 'users/sign-in.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('companies_list')


class RegisterView(FormView):
    template_name = 'users/sign-up.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('companies_list')

    def form_valid(self, form):
        user = form.save()  # Save the new User object
        Profile.objects.get_or_create(user=user)  # Automatically create a Profile for the new user
        login(self.request, user)  # Log the user in
        return redirect(self.get_success_url())  # Redirect to the success URL

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'users/profiles.html'
    context_object_name = 'profiles'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/form-profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/form-profile.html'
    success_url = reverse_lazy('profiles')

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('profiles')

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
