from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from esgmanager.models import ESGActionPlan
from esgmanager.forms import ESGActionPlanForm


class ListViewActionPlan(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = ESGActionPlan
    template_name = 'esgmanager/action_plan/action-plans.html'
    context_object_name = 'action_plans'


class DetailViewActionPlan(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = ESGActionPlan
    template_name = 'esgmanager/action_plan/action-plan.html'
    context_object_name = 'action_plan'


class CreateViewActionPlan(LoginRequiredMixin, CompanyContextMixin, CreateView):
    form_class = ESGActionPlanForm
    template_name = 'esgmanager/action_plan/form-action-plan.html'
    success_url = reverse_lazy('action_plans')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('action_plans')


class UpdateViewActionPlan(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = ESGActionPlan
    form_class = ESGActionPlanForm
    template_name = 'esgmanager/action_plan/form-action-plan.html'
    success_url = reverse_lazy('action_plans')


class DeleteViewActionPlan(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = ESGActionPlan
    template_name = 'esgmanager/delete-universal.html'
    success_url = reverse_lazy('action_plans')
