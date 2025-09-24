from django.views.generic import ListView
from dashboard_view.models import User
# Create your views here.

class DashboardLoginView(ListView):
    model = User