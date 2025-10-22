
from django.contrib import admin
from django.urls import path, include
from Assignement_Project_Blake_bmackin2.views import redirect_root_view

urlpatterns = [
    path('',redirect_root_view),
    path('administration/', admin.site.urls),
    path('', include('dashboard_view.urls')),
    path('', include('monitoring.urls')),
    path('', include('logging_app.urls'))
]
