from django import forms
from monitoring.models import ServiceType, Server


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