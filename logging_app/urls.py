from django.urls import path, include
from logging_app.views import LogEventsView

urlpatterns = [
    path('logs/',LogEventsView.as_view()),
]