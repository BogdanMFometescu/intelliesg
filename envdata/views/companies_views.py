from envdata.forms import CompanyForm
from envdata.models import Company
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from envdata.mixins import UpdateModeMixin


class CompanyListView(ListView):
    model = Company
    template_name = 'envdata/companies.html'
    context_object_name = 'companies'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'envdata/company.html'
    context_object_name = 'company'


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'envdata/form-company.html'
    success_url = reverse_lazy('companies')

    def form_valid(self, form):
        return super(CompanyCreateView, self).form_valid(form)


class CompanyUpdateView(UpdateModeMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'envdata/form-company.html'
    success_url = reverse_lazy('companies')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('companies')

