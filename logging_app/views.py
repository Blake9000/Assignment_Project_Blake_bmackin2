from django.shortcuts import get_object_or_404, render
from django.views import View
from logging_app.models import LogEvent
from django.views.generic import ListView



class LogEventsView(ListView):
    model = LogEvent
    context_object_name = 'log_events'
    template_name = "logging_app_view/logging_app_view.html"

class LogDetailView(View):

    def get(self, request, primary_key):
        log = get_object_or_404(LogEvent, pk=primary_key)
        source = log.source
        service = log.source.service_id

        return render(
            request,
            'logging_app_view/log_details.html',
            {
                'log': log,
                'source': source,
                'service': service
            }
        )
