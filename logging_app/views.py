from django.shortcuts import render
from logging_app.models import LogEvent

def log_events_view(request):
    logs = LogEvent.objects.all()
    return render(
        request,
        "logging_app_view/logging_app_view.html",
        {"logs": logs}
    )
