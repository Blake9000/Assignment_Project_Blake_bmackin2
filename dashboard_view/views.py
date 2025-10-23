from urllib import request

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import TemplateView, ListView, CreateView
from monitoring.models import Service, CheckResult, Server, Probe, ServiceType
from logging_app.models import LogSource
from .forms import ServiceTypeForm, ServerForm


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

class AdminLogSource(ListView):
    model = LogSource
    context_object_name = 'log_sources'
    template_name = 'dashboard_view/admin_log_sources.html'

class AdminMonitoringProbes(ListView):
    model = Probe
    context_object_name = 'monitoring_probes'
    template_name = 'dashboard_view/admin_monitoring_probes.html'

class AdminServiceTypes(ListView):
    model = ServiceType
    context_object_name = 'service_types'
    template_name = 'dashboard_view/admin_service_types.html'

class AdminService(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'dashboard_view/admin_services.html'


def service_type_add(request):
    if request.method == "POST":
        form = ServiceTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success!')
    else:
        form = ServiceTypeForm()
    return render(request, 'dashboard_view/partials/_service_types_form.html', {'form': form})

class ServerAdd(CreateView):
    model = Server
    form_class = ServerForm
    template_name = 'dashboard_view/partials/_server_form.html'


