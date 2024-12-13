from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from common.mixins import CompanyContextMixin, UpdateModeMixin
from esgmanager.models import ESGActionPlan, ESGActionPlanObjectives, ESGPillars
from esgmanager.forms import ESGActionPlanForm
from companies.models import Company


class ListViewActionPlan(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = ESGActionPlan
    template_name = 'esgmanager/action_plan/action-plans.html'
    context_object_name = 'action_plans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companies = Company.objects.prefetch_related(
            Prefetch('esgpillars_set', queryset=ESGPillars.objects.prefetch_related(Prefetch

                                                                                    ('esgactionplanobjectives_set',
                                                                                     queryset=ESGActionPlanObjectives.objects.prefetch_related(
                                                                                         'esgactionplanactions_set')))))
        print(companies)
        context['companies'] = companies
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        action_plan = context['action_plan']
        context['company'] = action_plan.company
        context['pillars'] = action_plan.pillar.company.esgpillars_set.all().prefetch_related(
            Prefetch('esgactionplanobjectives_set',
                     queryset=ESGActionPlanObjectives.objects.prefetch_related('esgactionplanactions_set'))
        )
        return context

    def get_object(self):
        action_plan_id = self.kwargs.get('pk')

        return ESGActionPlan.objects.select_related('company', 'pillar').prefetch_related(
            'esgactionplanobjectives_set__esgactionplanactions_set'
        ).get(id=action_plan_id)


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
