from companies.forms import CompanyForm
from companies.models import Company
from envdata.models import Fuel, NaturalGas, Sf6, Refrigerant, Energy, Travel, Waste, Target
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from common.mixins import UpdateModeMixin, CompanyContextMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView, CompanyContextMixin):
    template_name = 'starter.html'


class QuickStart(TemplateView, CompanyContextMixin):
    template_name = 'companies/quik_start.html'


class CompanyListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = Company
    template_name = 'companies/companies.html'
    context_object_name = 'companies_list'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return Company.objects.filter(profile__user=self.request.user)


class CompanyDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Company
    template_name = 'companies/single-company.html'
    context_object_name = 'single_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.kwargs.get('pk')
        emissions_data_by_year = {}

        # Collect emissions data by year
        try:
            for model in [Fuel, NaturalGas, Sf6, Refrigerant, Energy, Travel, Waste]:
                model_name = model.__name__.lower()
                model_data = model.annual_emissions(company_id)
                for data in model_data:
                    year = data['year']
                    total_co2 = data['total_co2']

                    if year not in emissions_data_by_year:
                        emissions_data_by_year[year] = {'total': 0}

                    # Add model-specific data
                    emissions_data_by_year[year][model_name] = emissions_data_by_year[year].get(model_name,
                                                                                                0) + total_co2
                    emissions_data_by_year[year]['total'] += total_co2

        except Exception as e:
            print(f"Error collecting emissions data: {e}")

        try:
            target_emission_per_year = Target.get_target_per_year(company_id)
            target_emission_per_year_str_keys = {str(year): target for year, target in target_emission_per_year.items()}

            for year in emissions_data_by_year:
                emissions_data_by_year[year]['target'] = target_emission_per_year_str_keys.get(year, "Base year")
        except Exception as e:
            print(f"Error merging target data: {e}")

        # Ensure each year entry has all keys
        for year, data in emissions_data_by_year.items():
            for key in ['fuel', 'naturalgas', 'refrigerant', 'sf6', 'travel', 'energy', 'waste']:
                if key not in data:
                    data[key] = 0  # or a suitable default value

        # Convert dictionary to a sorted list
        emissions_data = [dict(year=year, **data) for year, data in emissions_data_by_year.items()]
        emissions_data.sort(key=lambda x: x['year'])

        context['emissions_data'] = emissions_data
        return context


class CompanyCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/form-company.html'
    success_url = reverse_lazy('companies_list')

    def get_form_kwargs(self):
        kwargs = super(CompanyCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('companies_list')


class CompanyUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/form-company.html'
    success_url = reverse_lazy('companies_list')

    def get_form_kwargs(self):
        kwargs = super(CompanyUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


class CompanyDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Company
    template_name = 'companies/delete-universal.html'
    success_url = reverse_lazy('companies_list')
