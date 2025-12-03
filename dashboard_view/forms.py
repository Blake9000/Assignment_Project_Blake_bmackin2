from django import forms

from logging_app.models import LogSource
from monitoring.models import ServiceType, Server, Probe, Service
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = "__all__"

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_description(self):
        return self.cleaned_data['description'].strip()

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = "__all__"

    def clean_hostname(self):
        return self.cleaned_data['hostname'].strip()

    def clean_ip_address(self):
        return self.cleaned_data['ip_address'].strip()

    def clean_location(self):
        return self.cleaned_data['location'].strip()

    def clean_os(self):
        return self.cleaned_data['os'].strip()

class MonitoringProbesForm(forms.ModelForm):
    class Meta:
        model = Probe
        fields = "__all__"

    def clean_service(self):
        return self.cleaned_data['service']
    def clean_probe_type(self):
        return self.cleaned_data['probe_type'].strip()
    def clean_target(self):
        return self.cleaned_data['target'].strip()
    def clean_interval_seconds(self):
        return self.cleaned_data['interval_seconds']
    def clean_enabled(self):
        return self.cleaned_data['enabled']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
    def clean_server(self):
        return self.cleaned_data['server']
    def clean_type(self):
        return self.cleaned_data['type']
    def clean_name(self):
        return self.cleaned_data['name'].strip()
    def clean_port(self):
        return self.cleaned_data['port']
    def clean_config(self):
        return self.cleaned_data['config']

class LogSourceForm(forms.ModelForm):
    class Meta:
        model = LogSource
        fields = "__all__"
    def clean_service_id(self):
        return self.cleaned_data['service_id']
    def clean_source_type(self):
        return self.cleaned_data['source_type'].strip()
    def clean_path(self):
        return self.cleaned_data['path'].strip()
    def clean_parser(self):
        return self.cleaned_data['parser'].strip()
    def clean_ssh_key(self):
        return self.cleaned_data['ssh_key'].strip()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
        )
