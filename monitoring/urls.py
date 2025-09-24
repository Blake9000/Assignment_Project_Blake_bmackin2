from django.urls import path, include

from monitoring.views import MonitoringViews
urlpatterns = [
    path('dashboard/',MonitoringViews.as_view())
]