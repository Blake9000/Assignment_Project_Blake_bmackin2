from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, ListView
from monitoring.models import Service, CheckResult, Server

# Create your views here.

def dashboard_login_view(request):
    template = loader.get_template('dashboard_view/dashboard_view_login.html')
    output = template.render()
    return HttpResponse(output)


class AdminView(TemplateView):
    template_name = 'dashboard_view/admin_overview.html'


class AdminServers(ListView):
    model = Server
    context_object_name = 'servers'
    template_name = 'dashboard_view/admin_servers.html'