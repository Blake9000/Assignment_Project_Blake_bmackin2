from io import BytesIO
from django.shortcuts import get_object_or_404, render
from django.views import View
from logging_app.models import LogEvent
from django.views.generic import ListView
from django.db.models import Q, Count
import matplotlib.pyplot as plt
from django.http import HttpResponse

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
        ctx['total_logs'] = search_qs.count()
        ctx['total_unique'] = (
            search_qs.values('level').
            annotate(total=Count('level')).
            order_by('-total')
        )
        ctx['sizes'] = []
        ctx['labels'] = []
        for eventCt in ctx['total_unique']:
            ctx['sizes'].append(eventCt['total'])
            ctx['labels'].append(eventCt['level'])

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



def errors_pie_chart(request):
    q = request.GET.get('q')
    search_qs = LogEvent.objects.all()
    if q:
        search_qs = LogEvent.objects.filter(
            Q(message__icontains=q) | Q(level__icontains=q) | Q(source__service_id__server__hostname__icontains=q) | Q(
                timestamp__icontains=q))

    total_unique = search_qs.values('level').annotate(total=Count('level'))
    sizes = []
    labels = []

    for event in total_unique:
        sizes.append(event['total'])
        labels.append(event['level'])

    if sum(sizes) == 0:
        return HttpResponse()

    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.pie(sizes, labels=labels)
    ax.set_title("Log Event Frequency")
    fig.tight_layout()

    buf = BytesIO()

    fig.savefig(buf, format='png')

    plt.close(fig)
    buf.seek(0)


    return HttpResponse(buf.getvalue(), content_type='image/png')