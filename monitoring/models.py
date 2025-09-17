from django.db import models

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
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='services')
    type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=128)
    hostname = models.CharField(max_length=255)
    port = models.PositiveIntegerField()
    status = models.CharField(max_length=16, default="UNKNOWN") #I'm thinking I will use UP, DOWN, and UNKNOWN
    config = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.server.hostname}"

