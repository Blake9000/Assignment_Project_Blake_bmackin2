import socket
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from django.utils import timezone
import datetime
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from .models import LogSource, LogEvent

scheduler = BackgroundScheduler(timezone="UTC")
scheduler.add_jobstore(DjangoJobStore(), "default")

from time import time

def checkConnection():
    sock = socket.create_server((LogSource.service_id.server.ip_address,LogSource.service_id.port))