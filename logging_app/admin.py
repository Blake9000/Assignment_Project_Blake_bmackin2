from django.contrib import admin
from .models import LogSource, LogEvent
# Register your models here.

admin.site.register(LogSource)
admin.site.register(LogEvent)