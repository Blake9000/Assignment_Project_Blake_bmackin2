from django.views.generic import ListView
from dashboard_view.models import User
# Create your views here.

class DashboardLoginView(ListView):
    model = User
    template_name = "dashboard_view/dashboard_view_login.html"