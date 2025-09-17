from django.contrib import admin
from .models import Server,ServiceType, Service, Probe, CheckResult
# Register your models here.


admin.site.register(Server)
admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(Probe)
admin.site.register(CheckResult)