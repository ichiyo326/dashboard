from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class PerformanceResult(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    requests = models.IntegerField()
    avg_response_time_ms = models.FloatField()

class DashboardConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    layout = models.JSONField(default=list)
