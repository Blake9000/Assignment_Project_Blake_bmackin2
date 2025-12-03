from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.TextField(null=True, blank=True, default=None, editable=False)
    email = models.EmailField()
    role = models.CharField(max_length=5) # Owner, admin, user
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class LoginAudit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    username_attempted = models.CharField(max_length=128)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username_attempted}: {self.ip_address}"


