from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from esgmanager.models import ESGPillars
from esgmanager.forms import ESGPillarsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from common.mixins import UpdateModeMixin, CompanyContextMixin


class ListViewPillars(LoginRequiredMixin, ListView, CompanyContextMixin):
    model = ESGPillars
    template_name = 'esgmanager/pillars/pillars.html'
    context_object_name = 'pillars'

    def get_queryset(self):
        return ESGPillars.objects.all().order_by('pillar')


class DetailViewPillars(LoginRequiredMixin, DetailView, CompanyContextMixin):
    model = ESGPillars
    template_name = 'esgmanager/pillars/pillar.html'
    context_object_name = 'pillar'


class CreateViewPillars(LoginRequiredMixin, CreateView, CompanyContextMixin):
    model = ESGPillars
    form_class = ESGPillarsForm
    template_name = 'esgmanager/pillars/form-pillar.html'
    success_url = reverse_lazy('pillars')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pillars')


class UpdateViewPillars(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = ESGPillars
    form_class = ESGPillarsForm
    template_name = 'esgmanager/pillars/form-pillar.html'
    success_url = reverse_lazy('pillars')


class DeleteViewPillars(LoginRequiredMixin,CompanyContextMixin,DeleteView):
    model = ESGPillars
    template_name = 'esgmanager/delete-universal.html'
    success_url = reverse_lazy('pillars')





