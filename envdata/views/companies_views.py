from envdata.forms import CompanyForm
from envdata.models import Company
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView, CompanyContextMixin):
    template_name = 'starter.html'


class CompanyListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = Company
    template_name = 'envdata/companies.html'
    context_object_name = 'companies_list'


class CompanyDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Company
    template_name = 'envdata/single-company.html'
    context_object_name = 'single_company'


class CompanyCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'envdata/form-company.html'
    success_url = reverse_lazy('companies_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('companies_list')


class CompanyUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'envdata/form-company.html'
    success_url = reverse_lazy('companies_list')


class CompanyDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Company
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('companies_list')
