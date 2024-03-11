from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from envdata.models import Target
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.forms import TargetForm
from django.urls import reverse_lazy


class TargetListView(CompanyContextMixin, ListView):
    model = Target
    template_name = 'envdata/targets/targets.html'
    context_object_name = 'targets'

    def get_queryset(self):
        return Target.objects.all().order_by('base_year', 'intermediate_year', 'net_zero_year')


class TargetDetailView(CompanyContextMixin, DetailView):
    model = Target
    template_name = 'envdata/targets/target.html'
    context_object_name = 'target'


class TargetCreateView(CompanyContextMixin, CreateView):
    model = Target
    template_name = 'envdata/targets/form-target.html'
    form_class = TargetForm
    success_url = reverse_lazy('targets')

    def form_valid(self, form):
        return super().form_valid(form)


class TargetUpdateView(UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Target
    template_name = 'envdata/targets/form-target.html'
    form_class = TargetForm
    success_url = reverse_lazy('targets')


class TargetDeleteView(CompanyContextMixin, DeleteView):
    model = Target
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('targets')
