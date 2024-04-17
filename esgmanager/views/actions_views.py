from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from esgmanager.models import ESGActionPlanActions
from esgmanager.forms import ESGActionPlanActionsForm


class ListViewActions(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = ESGActionPlanActions
    template_name = 'esgmanager/action_plan_actions/actions.html'
    context_object_name = 'actions'


class DetailViewActions(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = ESGActionPlanActions
    template_name = 'esgmanager/action_plan_actions/action.html'
    context_object_name = 'action'


class CreateViewActions(LoginRequiredMixin, CompanyContextMixin, CreateView):
    form_class = ESGActionPlanActionsForm
    template_name = 'esgmanager/action_plan_actions/form-action.html'
    success_url = reverse_lazy('actions')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('actions')


class UpdateViewActions(LoginRequiredMixin, CompanyContextMixin, UpdateView, UpdateModeMixin):
    form_class = ESGActionPlanActionsForm
    template_name = 'esgmanager/action_plan_actions/form-action.html'
    success_url = reverse_lazy('actions')


class DeleteViewActions(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = ESGActionPlanActions
    template_name = 'esgmanager/delete-universal.html'
    success_url = reverse_lazy('actions')
