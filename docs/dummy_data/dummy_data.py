from monitoring.models import Server, ServiceType, Service, Probe, CheckResult
from logging_app.models import LogSource, LogEvent


CheckResult.objects.all().delete()
Probe.objects.all().delete()
Service.objects.all().delete()
ServiceType.objects.all().delete()
Server.objects.all().delete()
LogEvent.objects.all().delete()
LogSource.objects.all().delete()


srv1 = Server.objects.create(hostname="web-1", ip_address="192.168.1.10", location="Data Center A", os="Ubuntu 22.04")
srv2 = Server.objects.create(hostname="db-1", ip_address="192.168.1.20", location="Data Center B", os="Postgres Linux")


st_http = ServiceType.objects.create(name="HTTP", description="Web server")
st_db = ServiceType.objects.create(name="Postgres", description="Database server")


svc1 = Service.objects.create(server=srv1, type=st_http, name="Nginx", hostname="web-1.local", port=80, status="UP")
svc2 = Service.objects.create(server=srv2, type=st_db, name="PostgresDB", hostname="db-1.local", port=5432, status="DOWN")


probe1 = Probe.objects.create(service=svc1, probe_type="HTTP", target="http://web-1.local:80", interval_seconds=30, timeout_seconds=5)
probe2 = Probe.objects.create(service=svc2, probe_type="TCP", target="db-1.local:5432", interval_seconds=60, timeout_seconds=10)


CheckResult.objects.create(probe=probe1, timestamp="2025-09-17T10:00:00Z", result="UP", latency_ms=120, http_status=200)
CheckResult.objects.create(probe=probe1, timestamp="2025-09-17T10:05:00Z", result="DOWN", error="Timeout")
CheckResult.objects.create(probe=probe2, timestamp="2025-09-17T10:00:00Z", result="DOWN", error="Connection refused")


ls1 = LogSource.objects.create(service_id=svc1, source_type="file", path="/var/log/nginx/access.log", parser="nginx")
ls2 = LogSource.objects.create(service_id=svc2, source_type="syslog", path="/var/log/postgres/error.log", parser="postgres")


LogEvent.objects.create(source=ls1, timestamp="2025-09-17T10:10:00Z", level="INFO", message="Nginx started")
LogEvent.objects.create(source=ls1, timestamp="2025-09-17T10:15:00Z", level="ERROR", message="404 Not Found: /index.html")
LogEvent.objects.create(source=ls2, timestamp="2025-09-17T10:20:00Z", level="CRITICAL", message="Database connection lost")


