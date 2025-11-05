import io
import json
import urllib
from urllib import request

import matplotlib
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from django.apps import apps
from matplotlib import pyplot as plt

from monitoring.models import Service, CheckResult, Server, Probe, ServiceType
from logging_app.models import LogSource
from .forms import ServiceTypeForm, ServerForm, MonitoringProbesForm, ServiceForm, LogSourceForm


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
            return HttpResponse(f'<script>alert("Invalid Entry, fix errors: {form.errors.as_text().replace('\n','')}");</script>', headers={"HX-Reswap": "afterend"})
    else:
        form = ServiceTypeForm()
    return render(request, 'dashboard_view/partials/_service_types_form.html', {'form': form})

def monitoring_probe_add(request):
    if request.method == "POST":
        form = MonitoringProbesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success!')
        else:
            return HttpResponse(f'<script>alert("Invalid Entry, fix errors: {form.errors.as_text().replace('\n','')}");</script>', headers={"HX-Reswap": "afterend"})
    else:
        form = MonitoringProbesForm()
    return render(request, 'dashboard_view/partials/_monitoring_probes_form.html', {'form': form})

def server_add(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success!')
        else:
            return HttpResponse(f'<script>alert("Invalid Entry, fix errors: {form.errors.as_text().replace('\n','')}");</script>', headers={"HX-Reswap": "afterend"})
    else:
        form = ServerForm()
    return render(request, 'dashboard_view/partials/_server_form.html', {'form': form})


def service_add(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success!')
        else:
            return HttpResponse(f'<script>alert("Invalid Entry, fix errors: {form.errors.as_text().replace('\n','')}");</script>', headers={"HX-Reswap": "afterend"})
    else:
        form = ServiceForm()
    return render(request, 'dashboard_view/partials/_services_form.html', {'form': form})

def log_source_add(request):
    if request.method == "POST":
        form = LogSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success!')
        else:
            return HttpResponse(f'<script>alert("Invalid Entry, fix errors: {form.errors.as_text().replace('\n','')}");</script>', headers={"HX-Reswap": "afterend"})
    else:
        form = LogSourceForm()
    return render(request, 'dashboard_view/partials/_log_sources_form.html', {'form': form})

def generic_delete(request, app, model, pk):
    Model = apps.get_model(app_label=app, model_name=model)
    if Model is None:
        return HttpResponse(status=404)
    obj = Model.objects.filter(pk=pk).first()
    if not obj:
        return HttpResponse(status=404)
    obj.delete()
    return HttpResponse("", headers={"HX-Trigger": "deleted"})


class DashboardAPI(View):

    def get(self, request):
        q = request.GET.getlist('q')
        monitoringModels = {"service": Service.objects.all(), "server": Server.objects.all(), "probe": Probe.objects.all(), "service_type": ServiceType.objects.all()}
        logSourceModels = {"log_source": LogSource.objects.all()}
        qs = {}
        if q:
            for i in q:
                if i in monitoringModels:
                    qs.update({i: monitoringModels[i]})
                if i in logSourceModels:
                    qs.update({i: logSourceModels[i]})
        else:
            qs.update(monitoringModels)
            qs.update(logSourceModels)

        data = {key: list(value.values()) for key, value in qs.items()}

        return JsonResponse({"ok":True, "data":data})



def overviewChart(request):
    matplotlib.use('Agg')
    api_url = request.build_absolute_uri(reverse('api'))
    with urllib.request.urlopen(api_url) as response:
        payload = json.loads(response.read())

    rows = payload.get("data",[])

    labels = [r+'s' for r in rows]
    counts = []
    for r in rows:
        counts.append(len(payload["data"][r]))

    fig, ax = plt.subplots(figsize=(6,5),dpi=150)
    ax.bar(range(len(counts)), counts, tick_label=labels)
    ax.set_title("Overview")
    ax.set_ylabel("Count")
    fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf, content_type="image/png")


def weather(request):
    if request.method == "POST":
        params =request.POST.get("latitude")+","+request.POST.get("longitude")
        url = "https://api.weather.gov/points/" + params
        output_raw = False
        try:
            output_raw_info = requests.get(url)
            output_raw = requests.get(output_raw_info.json()['properties']['forecastHourly'])
        except requests.exceptions.RequestException as e:
            return JsonResponse({"ok":False, "error":str(e)})
        if output_raw:
            return JsonResponse({'ok':True,'data': output_raw.json()})
    return render(request, 'dashboard_view/weather.html')