from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from common.mixins import UpdateModeMixin, CompanyContextMixin
from esgmanager.models import ESGActionPlanObjectives
from esgmanager.forms import ESGActionPlanObjectivesForm


class ListViewObjectives(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = ESGActionPlanObjectives
    template_name = 'esgmanager/action_plan_objectives/objectives.html'
    context_object_name = 'objectives'


class DetailViewObjectives(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = ESGActionPlanObjectives
    template_name = 'esgmanager/action_plan_objectives/objective.html'
    context_object_name = 'objective'


class CreateViewObjectives(LoginRequiredMixin, CompanyContextMixin, CreateView):
    form_class = ESGActionPlanObjectivesForm
    template_name = 'esgmanager/action_plan_objectives/form-objective.html'
    success_url = reverse_lazy('objectives')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('objectives')


class UpdateViewObjectives(LoginRequiredMixin, CompanyContextMixin,UpdateModeMixin, UpdateView ):
    model = ESGActionPlanObjectives
    form_class = ESGActionPlanObjectivesForm
    template_name = 'esgmanager/action_plan_objectives/form-objective.html'
    success_url = reverse_lazy('objectives')


class DeleteViewObjectives(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = ESGActionPlanObjectives
    template_name = 'esgmanager/delete-universal.html'
    success_url = reverse_lazy('objectives')
