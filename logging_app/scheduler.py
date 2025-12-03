import socket
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from .models import LogSource, LogEvent
from monitoring import scheduler
import paramiko
from datetime import datetime
from django.utils import timezone


@register_job(
    scheduler.scheduler,
    "interval",
    seconds=60,
    jobstore="default",
    replace_existing=True,
    max_instances=1,
)
def pull_log():
    targets = LogSource.objects.all()

    for target in targets:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=target.service_id.server.ip_address,
            username="bmackin-admin",
            key_filename=target.ssh_key.path,
            port=22
        )
        sftp = client.open_sftp()
        try:
            with sftp.open(target.path) as f:
                data = f.read().decode("utf-8")
            for line in data.splitlines():
                split = line.split("]",3)
                if len(split) != 4:
                    continue
                time, level, src, msg = split
                time = time[1:].strip()
                dt = datetime.strptime(time, "%a %b %d %H:%M:%S.%f %Y")
                dt = timezone.make_aware(dt, timezone.get_current_timezone())
                if not LogEvent.objects.filter(source=target).exists():
                    LogEvent.objects.create(
                        source=target,
                        timestamp=dt,
                        level=level[2:].strip(),
                        err_src=src[1:].strip(),
                        message=msg.strip()
                    )
                else:
                    db_time = LogEvent.objects.filter(source=target).order_by("-timestamp").first().timestamp
                    if dt > db_time:
                        LogEvent.objects.create(
                            source=target,
                            timestamp=dt,
                            level=level[2:].strip(),
                            err_src=src[1:].strip(),
                            message=msg.strip()
                        )
        finally:
            sftp.close()
            client.close()
