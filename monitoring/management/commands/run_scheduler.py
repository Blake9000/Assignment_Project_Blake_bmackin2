from django.core.management.base import BaseCommand
from monitoring.scheduler import scheduler

class Command(BaseCommand):
    help = "Run APScheduler"

    def handle(self, *args, **options):
        if not scheduler.running:
            scheduler.start()

        self.stdout.write(self.style.SUCCESS("Scheduler started. Press CTRL+C to exit."))

        try:
            import time
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stdout.write("Stopping scheduler...")
            scheduler.shutdown()
