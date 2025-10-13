from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, View
from monitoring.models import Service, CheckResult
# Create your views here.

class MonitoringViews(ListView):
    model = Service
    context_object_name = 'services'
    template_name = "monitoring_view/monitoring_view.html"

class ServiceDetailView(View):

    def get(self, request, primary_key):
        service = get_object_or_404(Service, pk=primary_key)
        service_type = service.type
        server = service.server
        probe = service.probes.all()
        check_results = []
        for result in probe:
            check_results.append(result.results.all())
        return render(
            request,
            'monitoring_view/server_details.html',
            {
                'service': service,
                'service_type': service_type,
                'server': server,
                'probe': probe,
                'check_results': (
                    CheckResult.objects.filter(probe__service=service).select_related('probe').order_by('-timestamp')
                )
            }
        )

