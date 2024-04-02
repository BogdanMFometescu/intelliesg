from envdata.forms import CompanyForm
from envdata.models import Company, Fuel, NaturalGas, Sf6, Refrigerant, Energy, Travel, Waste, Target
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.kwargs.get('pk')
        emissions_data_by_year = {}

        try:
            for model in [Fuel, NaturalGas, Sf6, Refrigerant, Energy, Travel, Waste]:
                model_name = model.__name__.lower()
                model_data = model.annual_co2_per_company(company_id)
                for data in model_data:
                    year = data['year']
                    total_co2 = data['total_co2']

                    if year not in emissions_data_by_year:
                        emissions_data_by_year[year] = {'total': 0}

                    emissions_data_by_year[year][model_name] = total_co2
                    emissions_data_by_year[year]['total'] += total_co2
        except Exception as e:
            print(e)

        try:
            target_emission_per_year = Target.get_target_per_year(company_id)
        except Exception as e:
            print(e)
            target_emission_per_year = {}
        emissions_data = []
        for year, emissions in emissions_data_by_year.items():
            emissions['year'] = year
            emissions['target'] = target_emission_per_year.get(year,0)
            emissions_data.append(emissions)
            target_for_year = target_emission_per_year.get(year,
                                                       "Not set")  # or a default value like 0 if that makes more sense in your context
            emissions_data_by_year[year]['target'] = target_for_year

        emissions_data.sort(key=lambda x: x['year'])
        for item in emissions_data:
            print(f"Year: {item['year']}, Target: {item.get('target', 'Not set')}")
        context['emissions_data'] = emissions_data
        return context


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
