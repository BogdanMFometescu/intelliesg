from socialdata.models import HealthAndSafety
from socialdata.forms import HealthAndSafetyForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HealthAndSafetyListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = HealthAndSafety
    template_name = 'socialdata/health_and_safety/all-hs.html'
    context_object_name = 'hss'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return HealthAndSafety.objects.filter(profile__user=self.request.user)


class HealthAndSafetyDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = HealthAndSafety
    template_name = 'socialdata/health_and_safety/single-hs.html'
    context_object_name = 'hs'


class HealthAndSafetyCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = HealthAndSafety
    form_class = HealthAndSafetyForm
    template_name = 'socialdata/health_and_safety/form-hs.html'
    success_url = reverse_lazy('hss')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(HealthAndSafetyCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def get_success_url(self):
        return reverse_lazy('hss')


class HealthAndSafetyUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = HealthAndSafety
    form_class = HealthAndSafetyForm
    template_name = 'socialdata/health_and_safety/form-hs.html'
    success_url = reverse_lazy('hss')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile  # Ensure the profile is set to the current user's profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(HealthAndSafetyUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


class HealthAndSafetyDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = HealthAndSafety
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('hss')
