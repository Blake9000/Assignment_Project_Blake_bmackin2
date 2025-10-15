from django.urls import path, include
from logging_app.views import LogEventsView, LogDetailView
from logging_app.views import errors_pie_chart
urlpatterns = [
    path('logs/',LogEventsView.as_view(),
    name='logs'),
    path('logs/<int:primary_key>',LogDetailView.as_view(),
         name='logs-detail'),

    path("logs/errors-pie.png", errors_pie_chart, name="errors-pie"),

]