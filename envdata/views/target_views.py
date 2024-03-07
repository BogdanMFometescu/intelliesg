from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from envdata.models import Target
from envdata.mixins import UpdateModeMixin
from envdata.forms import TargetForm
from django.urls import reverse_lazy


class TargetListView(ListView):
    model = Target
    template_name = 'envdata/targets/targets.html'
    context_object_name = 'targets'


class TargetDetailView(DetailView):
    model = Target
    template_name = 'envdata/targets/target.html'
    context_object_name = 'target'


class TargetCreateView(CreateView):
    model = Target
    template_name = 'envdata/targets/form-target.html'
    form_class = TargetForm
    success_url = reverse_lazy('targets')

    def form_valid(self, form):
        return super().form_valid(form)


class TargetUpdateView(UpdateModeMixin, UpdateView):
    model = Target
    template_name = 'envdata/targets/form-target.html'
    form_class = TargetForm
    success_url = reverse_lazy('targets')


class TargetDeleteView(DeleteView):
    model = Target
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('targets')
