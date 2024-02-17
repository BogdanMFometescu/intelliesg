class UpdateModeMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_mode'] = True
        return context
