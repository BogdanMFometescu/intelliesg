from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin
from envdata.models import Waste
from envdata.forms import WasteForm


class WasteListView(ListView):
    model = Waste
    template_name = 'envdata/scope_two_emission/waste/wastes.html'
    context_object_name = 'wastes'


class WasteDetailView(DetailView):
    model = Waste
    template_name = 'envdata/scope_two_emission/waste/waste.html'
    context_object_name = 'waste'


class WasteCreateView(CreateView):
    model = Waste
    form_class = WasteForm
    template_name = 'envdata/scope_two_emission/waste/form-waste.html'
    success_url = reverse_lazy('wastes')

    def form_valid(self, form):
        return super(CreateView).form_valid(form)


class WasteUpdateView(UpdateModeMixin, UpdateView):
    mode = Waste
    form_class = WasteForm
    template_name = 'envdata/scope_two_emission/waste/form-waste.html'
    success_url = reverse_lazy('wastes')


class WasteDeleteView(DeleteView):
    model = Waste
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('wastes')
