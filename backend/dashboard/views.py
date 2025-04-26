from rest_framework import viewsets, permissions
from .models import PerformanceResult, DashboardConfig
from .serializers import PerformanceResultSerializer, DashboardConfigSerializer

class PerformanceResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PerformanceResult.objects.all().order_by('-timestamp')
    serializer_class = PerformanceResultSerializer
    permission_classes = [permissions.IsAdminUser]

class DashboardConfigViewSet(viewsets.ModelViewSet):
    serializer_class = DashboardConfigSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'put', 'patch']

    def get_queryset(self):
        return DashboardConfig.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 初回作成時に user を設定
        serializer.save(user=self.request.user)