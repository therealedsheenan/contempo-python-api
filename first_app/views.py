from first_app.models import AccessRecord
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['access_records'] = AccessRecord.objects.order_by('date')
        context['site_name'] = 'Site Name'
        return context

