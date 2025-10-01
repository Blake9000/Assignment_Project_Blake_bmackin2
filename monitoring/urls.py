from django.urls import path, include

from monitoring.views import MonitoringViews, ServiceDetailView
urlpatterns = [
    path('dashboard/',MonitoringViews.as_view(), name='dashboard'),

    path('dashboard/<int:primary_key>',ServiceDetailView.as_view(),name='service-detail')
]