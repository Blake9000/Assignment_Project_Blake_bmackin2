from django.urls import path, include
from dashboard_view.views import dashboard_login_view
from dashboard_view.views import AdminView

urlpatterns = [
    path('login/',dashboard_login_view, name='login'),
    path('admin/',AdminView.as_view(), name='admin'),
]
