from django.contrib import admin
from .models import User,LoginAudit
# Register your models here.

admin.site.register(User)
admin.site.register(LoginAudit)