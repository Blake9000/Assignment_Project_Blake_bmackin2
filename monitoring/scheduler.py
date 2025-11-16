from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from django.utils import timezone
import datetime
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from .models import Probe, CheckResult


scheduler = BackgroundScheduler(timezone="UTC")
scheduler.add_jobstore(DjangoJobStore(), "default")

#Jobs Here

from time import time

def pingIP(ip):
    ping = IP(dst=ip)/ICMP()
    start = time()
    reply = sr1(ping, timeout=1, verbose=False)
    end = time()
    if reply:
        latency_ms = (end - start) * 1000
        return reply, latency_ms
    return None, None

@register_job(
    scheduler,
    "interval",
    seconds=5,
    jobstore="default",
    replace_existing=True,
    max_instances=1,
)
def ping_orchestrator():
    now = timezone.now()
    targets = Probe.objects.filter(enabled=True).filter(probe_type="ping")

    for target in targets:
        if target.is_due(now):
            reply,latency = pingIP(target.target)
            if reply:
                result = "UP"
                extra = {
                    "response_ip": reply[IP].src,
                    "ttl": reply.ttl,
                    "icmp_type": reply[ICMP].type,
                    "icmp_code": reply[ICMP].code,
                }
            else:
                result = "DOWN"
                extra = {}
            CheckResult.objects.create(
                probe=target,
                timestamp=now,
                result=result,
                latency_ms=latency,
                extra=extra,
                error=None,
            )
            service = target.service
            service.status = result
            service.save(update_fields=["status"])

