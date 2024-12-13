from socialdata.models import EmployeeByContracts, NewEmployeeByAge, RotationRateOfEmployeeByAge, RetirementRate
from socialdata.forms import EmployeeByContractsForm, NewEmployeeByAgeForm, RotationRateOfEmployeeByAgeForm, \
    RetirementRateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from common.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .filters import EmployeeContractsFilter, NewEmployeeByAgeFilter
from django_filters.views import FilterView
from django.db.models import Sum, F


class EmployeeByContractsListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = EmployeeByContracts
    filterset_class = EmployeeContractsFilter
    template_name = 'socialdata/employees/contracts/contracts.html'
    context_object_name = 'contracts'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return EmployeeByContracts.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_full_time_contracts = \
            self.filterset.qs.annotate(total_contracts=F('full_time_women') + F('full_time_men')).aggregate(
                total_contract_full=Sum('total_contracts'))['total_contract_full'] or 0

        filtered_fixed_term_contracts = self.filterset.qs.annotate(
            total_contracts_ft=F('fixed_term_contract_women') + F('fixed_term_contract_men')).aggregate(
            total_contract_fixed=Sum('total_contracts_ft'))['total_contract_fixed'] or 0

        filtered_part_time_contracts = self.filterset.qs.annotate(
            total_contracts_pt=F('part_time_women') + F('part_time_men')).aggregate(
            total_contract_part=Sum('total_contracts_pt'))['total_contract_part'] or 0

        filtered_total_contracts = self.filterset.qs.annotate(
            total_company_contracts=F('part_time_women') + F('part_time_men') + F('full_time_women') + F(
                'full_time_men') + F('fixed_term_contract_women') + F('fixed_term_contract_men')).aggregate(
            total=Sum('total_company_contracts'))['total'] or 0

        context['full_time_contracts_display'] = filtered_full_time_contracts
        context['fixed_term_contracts_display'] = filtered_fixed_term_contracts
        context['part_time_contracts_display'] = filtered_part_time_contracts
        context['total_contracts_display'] = filtered_total_contracts
        return context


class EmployeeByContractsDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = EmployeeByContracts
    template_name = 'socialdata/employees/contracts/contract.html'
    context_object_name = 'contract'


class EmployeeByContractsCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = EmployeeByContracts
    form_class = EmployeeByContractsForm
    template_name = 'socialdata/employees/contracts/form-contracts.html'
    success_url = reverse_lazy('contracts')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EmployeeByContractsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def get_success_url(self):
        return reverse_lazy('contracts')


class EmployeeByContractsUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = EmployeeByContracts
    form_class = EmployeeByContractsForm
    template_name = 'socialdata/employees/contracts/form-contracts.html'
    success_url = reverse_lazy('contracts')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile  # Ensure the profile is set to the current user's profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EmployeeByContractsUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


class EmployeeByContractsDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = EmployeeByContracts
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('contracts')


class NewEmployeeByAgeListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = NewEmployeeByAge
    filterset_class = NewEmployeeByAgeFilter
    template_name = 'socialdata/employees/age/employees-ages.html'
    context_object_name = 'employees'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return NewEmployeeByAge.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_under_30 = \
            self.filterset.qs.annotate(total_under_30=F('men_under_30') + F('women_under_30')).aggregate(
                total_emp_under_30=Sum('total_under_30'))['total_emp_under_30'] or 0

        filtered_between_30_and_50 = self.filterset.qs.annotate(
            total_between_30_and_50=F('men_between_30_and_50') + F('women_between_30_and_50')).aggregate(
            total_30_and_50=Sum('total_between_30_and_50'))['total_30_and_50'] or 0

        filtered_over_50 = self.filterset.qs.annotate(total_over_50=F('men_over_50') + F('women_over_50')).aggregate(
            total_over=Sum('total_over_50'))['total_over'] or 0

        filtered_total_employees_by_age = self.filterset.qs.annotate(
            total_employees=F('men_under_30') + F('women_under_30') + F('men_between_30_and_50') + F(
                'women_between_30_and_50') + F('men_over_50') + F('women_over_50')).aggregate(
            total=Sum('total_employees'))['total'] or 0

        context['total_under_30_display'] = filtered_under_30
        context['total_between_30_and_50_display'] = filtered_between_30_and_50
        context['total_over_50'] = filtered_over_50
        context['total_employees_display'] = filtered_total_employees_by_age

        return context


class NewEmployeeByAgeDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = NewEmployeeByAge
    template_name = 'socialdata/employees/age/employees-age.html'
    context_object_name = 'employee'


class NewEmployeeByAgeCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = NewEmployeeByAge
    form_class = NewEmployeeByAgeForm
    template_name = 'socialdata/employees/age/form-age.html'
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(NewEmployeeByAgeCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def get_success_url(self):
        return reverse_lazy('employees')


class NewEmployeeByAgeUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = NewEmployeeByAge
    form_class = NewEmployeeByAgeForm
    template_name = 'socialdata/employees/age/form-age.html'
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile  # Ensure the profile is set to the current user's profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(NewEmployeeByAgeUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


class NewEmployeeByAgeDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = NewEmployeeByAge
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('employees')


class RotationRateOfEmployeeByAgeListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = RotationRateOfEmployeeByAge
    template_name = 'socialdata/employees/rotations/rotations.html'
    context_object_name = 'rotations'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return RotationRateOfEmployeeByAge.objects.filter(profile__user=self.request.user)


class RotationRateOfEmployeeByAgeDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = RotationRateOfEmployeeByAge
    template_name = 'socialdata/employees/rotations/rotation.html'
    context_object_name = 'rotation'


class RotationRateOfEmployeeByAgeCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = RotationRateOfEmployeeByAge
    form_class = RotationRateOfEmployeeByAgeForm
    template_name = 'socialdata/employees/rotations/form-rotations.html'
    success_url = reverse_lazy('rotations')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(RotationRateOfEmployeeByAgeCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def get_success_url(self):
        return reverse_lazy('rotations')


class RotationRateOfEmployeeByAgeUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = RotationRateOfEmployeeByAge
    form_class = RotationRateOfEmployeeByAgeForm
    template_name = 'socialdata/employees/rotations/form-rotations.html'
    success_url = reverse_lazy('rotations')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile  # Ensure the profile is set to the current user's profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(RotationRateOfEmployeeByAgeUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


class RotationRateOfEmployeeByAgeDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = RotationRateOfEmployeeByAge
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('rotations')


class RetirementRateListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = RetirementRate
    template_name = 'socialdata/employees/retirements/retirements.html'
    context_object_name = 'rotations'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return RotationRateOfEmployeeByAge.objects.filter(profile__user=self.request.user)


class RetirementRateDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = RetirementRate
    template_name = 'socialdata/employees/retirements/retirement.html'
    context_object_name = 'retirement'


class RetirementRateCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = RetirementRate
    form_class = RetirementRateForm
    template_name = 'socialdata/employees/retirements/form-retirements.html'
    success_url = reverse_lazy('retirements')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(RetirementRateCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def get_success_url(self):
        return reverse_lazy('retirements')


class RetirementRateUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = RetirementRate
    form_class = RetirementRateForm
    template_name = 'socialdata/employees/retirements/form-retirements.html'
    success_url = reverse_lazy('retirements')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile  # Ensure the profile is set to the current user's profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(RetirementRateUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


class RetirementRateDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = RetirementRate
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('retirements')
