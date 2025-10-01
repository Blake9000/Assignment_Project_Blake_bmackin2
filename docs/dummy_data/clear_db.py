from monitoring.models import Server, ServiceType, Service, Probe, CheckResult
from logging_app.models import LogSource, LogEvent


CheckResult.objects.all().delete()
Probe.objects.all().delete()
Service.objects.all().delete()
ServiceType.objects.all().delete()
Server.objects.all().delete()
LogEvent.objects.all().delete()
LogSource.objects.all().delete()

print("DB Cleared")