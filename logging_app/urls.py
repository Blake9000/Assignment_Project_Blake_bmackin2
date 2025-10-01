from django.urls import path, include
from logging_app.views import LogEventsView, LogDetailView

urlpatterns = [
    path('logs/',LogEventsView.as_view(),
    name='logs'),
    path('logs/<int:primary_key>',LogDetailView.as_view(),
         name='logs-detail')
]