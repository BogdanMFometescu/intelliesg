from envdata.models import Company
from django.views.generic.base import ContextMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin


class UpdateModeMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_mode'] = True
        return context


class CompanyContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        return context


# class UserGroupRequiredMixin:
#     """
#     Mixin to check if a user belongs to a specific group.
#     """
#     allowed_groups = []  # Define this in the views using this mixin
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             raise PermissionDenied
#
#         if request.user.is_superuser:
#             return super().dispatch(request, *args, **kwargs)
#
#         user_groups = request.user.groups.values_list('name', flat=True)
#         if not any(group in self.allowed_groups for group in user_groups):
#             raise PermissionDenied
#
#         return super().dispatch(request, *args, **kwargs)

