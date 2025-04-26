from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dashboard.views import PerformanceResultViewSet, DashboardConfigViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'performance', PerformanceResultViewSet, basename='performance')
router.register(r'dashboard-config', DashboardConfigViewSet, basename='dashboard-config')

urlpatterns = [
    path('admin/', admin.site.urls),

    # API のルーティング
    path('api/', include(router.urls)),

    # JWT 認証エンドポイント
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
