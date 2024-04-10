from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Waste
from envdata.forms import WasteForm
from .filters import WasteTypeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.db.models import Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class WasteListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Waste
    filterset_class = WasteTypeFilter
    template_name = 'envdata/scope_two_emission/waste/wastes.html'
    context_object_name = 'wastes'
    paginate_by = 50

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(co2_for_waste=F('quantity_disposed') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_waste'))['total_co2'] or 0
        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            wastes = paginator.page(page)
        except PageNotAnInteger:
            wastes = paginator.page(1)
        except EmptyPage:
            wastes = paginator.page(paginator.num_pages)

        context['wastes'] = wastes
        context['total_co2'] = filtered_qs

        return context


class WasteDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Waste
    template_name = 'envdata/scope_two_emission/waste/waste.html'
    context_object_name = 'waste'


class WasteCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Waste
    form_class = WasteForm
    template_name = 'envdata/scope_two_emission/waste/form-waste.html'
    success_url = reverse_lazy('wastes')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('wastes')


class WasteUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    mode = Waste
    form_class = WasteForm
    template_name = 'envdata/scope_two_emission/waste/form-waste.html'
    success_url = reverse_lazy('wastes')


class WasteDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Waste
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('wastes')
