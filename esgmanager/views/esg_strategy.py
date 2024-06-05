from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from esgmanager.models import ESGStrategy
from esgmanager.forms import StrategyForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.mixins import UpdateModeMixin, CompanyContextMixin


class ListViewStrategy(LoginRequiredMixin, CompanyContextMixin,ListView ):
    model = ESGStrategy
    template_name = 'esgmanager/esg_strategy/esg-strategies.html'
    context_object_name = 'strategies'


class DetailViewStrategy(LoginRequiredMixin, DetailView, CompanyContextMixin):
    model = ESGStrategy
    template_name = 'esgmanager/esg_strategy/esg-strategy.html'
    context_object_name = 'strategy'


class CreateViewStrategy(LoginRequiredMixin, CreateView, CompanyContextMixin):
    model = ESGStrategy
    form_class = StrategyForm
    template_name = 'esgmanager/esg_strategy/form-esg-strategy.html'
    success_url = reverse_lazy('strategies')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('strategies')


class UpdateViewStrategy(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = ESGStrategy
    form_class = StrategyForm
    template_name = 'esgmanager/esg_strategy/form-esg-strategy.html'
    success_url = reverse_lazy('strategies')


class DeleteViewStrategy(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = ESGStrategy
    template_name = 'esgmanager/delete-universal.html'
    success_url = reverse_lazy('strategies')
