from django.views.generic import ListView
from monitoring.models import Service
# Create your views here.

class MonitoringViews(ListView):
    model = Service
    context_object_name = 'services'
    template_name = "monitoring_view/monitoring_view.html"