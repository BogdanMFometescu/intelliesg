from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from common.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import PurchasedGoodsAndServices
from envdata.forms import PurchasedGoodsAndServicesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import PurchasedGoodsFilter
from django.db.models import Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PurchasedGoodsListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = PurchasedGoodsAndServices
    filterset_class = PurchasedGoodsFilter
    template_name = 'envdata/scope_three_emissions/purchase_goods/purchased-goods.html'
    context_object_name = 'purchased_goods'
    paginate_by = 50

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return PurchasedGoodsAndServices.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(co2_for_purchased_goods=F('quantity') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_purchased_goods'))['total_co2'] or 0

        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            purchased_goods = paginator.page(page)
        except PageNotAnInteger:
            purchased_goods  = paginator.page(1)
        except EmptyPage:
            purchased_goods  = paginator.page(paginator.num_pages)

        context['purchased_goods'] = purchased_goods 
        context['total_co2'] = filtered_qs

        return context


class PurchasedGoodsDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = PurchasedGoodsAndServices
    template_name = 'envdata/scope_three_emissions/purchase_goods/purchased-good.html'
    context_object_name = 'purchased_good'


class PurchasedGoodsCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = PurchasedGoodsAndServices
    form_class = PurchasedGoodsAndServicesForm
    template_name = 'envdata/scope_three_emissions/purchase_goods/form-purchased-goods.html'
    success_url = reverse_lazy('purchased_goods')

    def get_form_kwargs(self):
        kwargs = super(PurchasedGoodsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)



class PurchasedGoodsUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = PurchasedGoodsAndServices
    form_class = PurchasedGoodsAndServicesForm
    template_name = 'envdata/scope_three_emissions/purchase_goods/form-purchased-goods.html'
    success_url = reverse_lazy('purchased_goods')


class PurchasedGoodsDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = PurchasedGoodsAndServices
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('purchased_goods')
