from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from envdata.models import Target
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.forms import TargetForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TargetListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = Target
    template_name = 'envdata/targets/targets.html'
    context_object_name = 'targets'

    def get_queryset(self):
        return Target.objects.all().order_by('base_year', 'intermediate_year', 'net_zero_year')


class TargetDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Target
    template_name = 'envdata/targets/target.html'
    context_object_name = 'target'


class TargetCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Target
    template_name = 'envdata/targets/form-target.html'
    form_class = TargetForm
    success_url = reverse_lazy('targets')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('targets')


class TargetUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Target
    template_name = 'envdata/targets/form-target.html'
    form_class = TargetForm
    success_url = reverse_lazy('targets')


class TargetDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Target
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('targets')
