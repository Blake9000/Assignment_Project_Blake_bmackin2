from django.urls import path, include

from logging_app.views import LogViews
urlpatterns = [
    path('logs/',LogViews.as_view())
]