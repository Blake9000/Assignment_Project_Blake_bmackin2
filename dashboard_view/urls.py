from django.urls import path, include

import dashboard_view
from dashboard_view.views import dashboard_login_view
urlpatterns = [
    path('login/',dashboard_login_view)
]
