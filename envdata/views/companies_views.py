from envdata.forms import CompanyForm
from envdata.models import Company
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from django.views.generic import TemplateView


class HomePageView(TemplateView, CompanyContextMixin):
    template_name = 'starter.html'


class CompanyListView(CompanyContextMixin, ListView):
    model = Company
    template_name = 'envdata/companies.html'
    context_object_name = 'companies_list'


class CompanyDetailView(CompanyContextMixin, DetailView):
    model = Company
    template_name = 'envdata/single-company.html'
    context_object_name = 'single_company'


class CompanyCreateView(CompanyContextMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'envdata/form-company.html'
    success_url = reverse_lazy('companies_list')

    def form_valid(self, form):
        return super().form_valid(form)


class CompanyUpdateView(UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'envdata/form-company.html'
    success_url = reverse_lazy('companies_list')


class CompanyDeleteView(CompanyContextMixin, DeleteView):
    model = Company
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('companies_list')
