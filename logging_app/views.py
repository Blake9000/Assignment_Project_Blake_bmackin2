from django.shortcuts import get_object_or_404, render
from django.views import View
from logging_app.models import LogEvent
from django.views.generic import ListView
from django.db.models import Q


class LogEventsView(ListView):
    model = LogEvent
    context_object_name = 'log_events'
    template_name = "logging_app_view/logging_app_view.html"



    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q:
            search_qs = LogEvent.objects.filter(Q(message__icontains=q) | Q(level__icontains=q)|Q(source__service_id__server__hostname__icontains=q)|Q(timestamp__icontains=q))
        else:
            search_qs = LogEvent.objects.all()
        ctx['log_events'] = search_qs
        ctx['q'] = q
        return ctx



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
