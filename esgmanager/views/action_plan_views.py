from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from esgmanager.models import ESGActionPlan, ESGActionPlanObjectives
from esgmanager.forms import ESGActionPlanForm


class ListViewActionPlan(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = ESGActionPlan
    template_name = 'esgmanager/action_plan/action-plans.html'
    context_object_name = 'action_plans'

    def get_queryset(self):
        objectives_prefetched = Prefetch('esgactionplanobjectives_set',
                                         queryset=ESGActionPlanObjectives.objects.all().prefetch_related(
                                             'esgactionplanactions_set'))
        queryset = super().get_queryset().select_related('company', 'pillar').prefetch_related(objectives_prefetched)
        return queryset


class DetailViewActionPlan(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = ESGActionPlan
    template_name = 'esgmanager/action_plan/action-plan.html'
    context_object_name = 'action_plan'

    def get_object(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('company', 'pillar').prefetch_related(
            'esgactionplanobjectives_set__esgactionplanactions_set'
        )
        return queryset.get(pk=self.kwargs.get('pk'))


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
