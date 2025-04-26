from rest_framework import serializers
from .models import PerformanceResult, DashboardConfig

class PerformanceResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceResult
        fields = ['id', 'timestamp', 'requests', 'avg_response_time_ms']

class DashboardConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardConfig
        fields = ['layout']