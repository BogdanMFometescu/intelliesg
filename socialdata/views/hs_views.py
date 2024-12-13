from socialdata.models import HealthAndSafety
from socialdata.forms import HealthAndSafetyForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from common.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .filters import HealthAndSafetyFilter
from django_filters.views import FilterView
from django.db.models import Sum, F


class HealthAndSafetyListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = HealthAndSafety
    filterset_class = HealthAndSafetyFilter
    template_name = 'socialdata/health_and_safety/all-hs.html'
    context_object_name = 'hss'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return HealthAndSafety.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = self.filterset.qs.annotate(total_wh=F('total_working_hours')).aggregate(
            total_hours=Sum('total_wh'))['total_hours'] or 0

        filtered_qs_ep = self.filterset.qs.annotate(total_wh_ep=F('ep_total_working_hours')).aggregate(
            total_hours_ep=Sum('total_wh_ep'))['total_hours_ep'] or 0

        filtered_qs_training = \
            self.filterset.qs.annotate(total_training=F('total_training_hours')).aggregate(total=Sum('total_training'))[
                'total'] or 0
        context['total_working_hours_display'] = filtered_qs
        context['total_working_hours_display_ep'] = filtered_qs_ep
        context['total_training_hours_display'] = filtered_qs_training
        return context


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
