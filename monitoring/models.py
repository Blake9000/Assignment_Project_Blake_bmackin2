from django.db import models
from django.utils import timezone

# Create your models here.
class Server(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=255,blank=True)
    os = models.CharField(max_length=128,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hostname


class ServiceType(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    STATUS_CHOICES = (
        ("UP", 'Up'),
        ("DOWN", 'Down'),
        ("UNKNOWN", 'Unknown'),
    )
    server = models.ForeignKey(Server, on_delete=models.PROTECT, related_name='services')
    type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, related_name='services')
    hostname = models.ForeignKey(Server, on_delete=models.PROTECT, related_name='hostname_services')
    name = models.CharField(max_length=128)
    port = models.PositiveIntegerField()
    status = models.CharField(max_length=16,choices=STATUS_CHOICES, default="UNKNOWN", blank=True)
    config = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.server.hostname}"

class Probe(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='probes')
    probe_type = models.CharField(max_length=16)  # Some types can be ping, TCP, HTTP, etc
    target = models.CharField(max_length=512)     # Depends on the type of probe. For HTTP, it can be the URL, host:port for others
    interval_seconds = models.PositiveIntegerField(default=30)      # Time between "Heartbeats"
    enabled = models.BooleanField(default=True)
    last_ping = models.DateTimeField(null=True, blank=True)
    settings = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_due(self,now=None):
        if not self.enabled:
            return False
        if now is None:
            now = timezone.now()
        if self.last_ping is None:
            return True
        elapsed = (now - self.last_ping).total_seconds()
        return elapsed >= self.interval_seconds

    def __str__(self):
        return f"{self.probe_type} {self.target}"

class CheckResult(models.Model):
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE, related_name='results')
    timestamp = models.DateTimeField()
    result = models.CharField(max_length=8) # Up, down
    latency_ms = models.PositiveIntegerField(null=True, blank=True)
    http_status = models.PositiveIntegerField(null=True, blank=True)
    error = models.TextField(blank=True, null=True)
    extra = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.probe} {self.result}"



