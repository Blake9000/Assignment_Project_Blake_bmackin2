from django.urls import path, include

from logging_app.views import log_events_view
urlpatterns = [
    path('logs/',log_events_view)
]