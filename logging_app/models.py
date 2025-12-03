from django.db import models
from monitoring.models import Service


# Create your models here.
class LogSource(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='logs')
    source_type = models.CharField(max_length=16)
    path = models.TextField() # Where the log comes from
    ssh_key = models.TextField(null=True)
    parser = models.CharField(max_length=128, blank=True) # For future processing, what format is the log in?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} {self.path}"


class LogEvent(models.Model):
    source = models.ForeignKey(LogSource, on_delete=models.CASCADE, related_name='events')
    timestamp = models.DateTimeField()
    level = models.CharField(max_length=16) # error, info, warn, critical, etc
    message = models.TextField()

    def __str__(self):
        return f"{self.level}: {self.message}"
