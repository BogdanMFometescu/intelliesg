from esgmanager.models import SocialRisk
from esgmanager.forms import SocialRisksForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from common.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class SocialRiskListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = SocialRisk
    template_name = 'esgmanager/risks/social/soc-risks.html'
    context_object_name = 'soc_risks'


class SocialRiskDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = SocialRisk
    template_name = 'esgmanager/risks/social/soc-risk.html'
    context_object_name = 'soc_risk'


class SocialRiskCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    form_class = SocialRisksForm
    template_name = 'esgmanager/risks/social/form-soc-risk.html'
    success_url = reverse_lazy('soc_risks')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('soc_risks')


class SocialRiskUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateView, UpdateModeMixin):
    model = SocialRisk
    form_class = SocialRisksForm
    template_name = 'esgmanager/risks/social/form-soc-risk.html'
    success_url = reverse_lazy('soc_risks')


class SocialRiskDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = SocialRisk
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('soc_risks')
