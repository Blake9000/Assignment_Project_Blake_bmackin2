from django.urls import path, include
from dashboard_view.views import dashboard_login_view
from dashboard_view.views import SettingsView

urlpatterns = [
    path('login/',dashboard_login_view, name='login'),
    path('settings/',SettingsView.as_view(), name='settings'),
]
