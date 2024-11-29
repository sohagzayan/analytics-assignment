from django.urls import path
from .views import AnalyticsAPI

urlpatterns = [
    path("analytics/", AnalyticsAPI.as_view(), name="analytics_api"),
]
