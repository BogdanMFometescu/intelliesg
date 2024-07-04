from socialdata.models import EmployeeByContracts, NewEmployeeByAge, RotationRateOfEmployeeByAge, RetirementRate
from socialdata.forms import EmployeeByContractsForm, NewEmployeeByAgeForm, RotationRateOfEmployeeByAgeForm, \
    RetirementRateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class EmployeeByContractsListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = EmployeeByContracts
    template_name = ''
    context_object_name = 'contracts'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return EmployeeByContracts.objects.filter(profile__user=self.request.user)


class EmployeeByContractsDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = EmployeeByContracts
    template_name = ''
    context_object_name = 'contract'


class EmployeeByContractsCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = EmployeeByContracts
    form_class = EmployeeByContractsForm
    template_name = ''
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


class EmployeeByContractsUpdateView(LoginRequiredMixin, CompanyContextMixin, CreateView, UpdateView):
    model = EmployeeByContracts
    form_class = EmployeeByContractsForm
    template_name = ''
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


class NewEmployeeByAgeListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = NewEmployeeByAge
    template_name = ''
    context_object_name = 'employees'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return NewEmployeeByAge.objects.filter(profile__user=self.request.user)


class NewEmployeeByAgeDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = NewEmployeeByAge
    template_name = ''
    context_object_name = 'employee'


class NewEmployeeByAgeCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = NewEmployeeByAge
    form_class = NewEmployeeByAgeForm
    template_name = ''
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


class NewEmployeeByAgeUpdateView(LoginRequiredMixin, CompanyContextMixin, CreateView, UpdateView):
    model = NewEmployeeByAge
    form_class = NewEmployeeByAgeForm
    template_name = ''
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
    template_name = ''
    context_object_name = 'rotations'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return RotationRateOfEmployeeByAge.objects.filter(profile__user=self.request.user)


class RotationRateOfEmployeeByAgeDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = RotationRateOfEmployeeByAge
    template_name = ''
    context_object_name = 'rotation'


class RotationRateOfEmployeeByAgeCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = RotationRateOfEmployeeByAge
    form_class = RotationRateOfEmployeeByAgeForm
    template_name = ''
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


class RotationRateOfEmployeeByAgeUpdateView(LoginRequiredMixin, CompanyContextMixin, CreateView, UpdateView):
    model = RotationRateOfEmployeeByAge
    form_class = RotationRateOfEmployeeByAgeForm
    template_name = ''
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
    template_name = ''
    context_object_name = 'rotations'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return RotationRateOfEmployeeByAge.objects.filter(profile__user=self.request.user)


class RetirementRateDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = RetirementRate
    template_name = ''
    context_object_name = 'retirement'


class RetirementRateCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = RetirementRate
    form_class = RetirementRateForm
    template_name = ''
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


class RetirementRateUpdateView(LoginRequiredMixin, CompanyContextMixin, CreateView, UpdateView):
    model = RetirementRate
    form_class = RetirementRateForm
    template_name = ''
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
