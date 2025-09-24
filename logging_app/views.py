from django.views.generic import ListView
from logging_app.models import LogEvent
# Create your views here.

class LogViews(ListView):
    model = LogEvent
    template_name = "logging_app_view/logging_app_view.html"