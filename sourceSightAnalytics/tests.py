from django.test import TestCase
from django.urls import reverse
from .models import Visitor

class AnalyticsAPITestCase(TestCase):
    def setUp(self):
        Visitor.objects.bulk_create([
            Visitor(date="2023-11-01", source="facebook", count=100),
            Visitor(date="2023-11-01", source="google", count=200),
            Visitor(date="2023-11-02", source="instagram", count=150),
        ])

    def test_last_7_days(self):
        response = self.client.get(reverse("analytics_api"), {"range_type": "last_7_days"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

    def test_custom_date_range(self):
        response = self.client.get(reverse("analytics_api"), {
            "range_type": "custom",
            "start_date": "2023-11-01",
            "end_date": "2023-11-02",
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

    def test_cache_hit(self):
        self.client.get(reverse("analytics_api"), {"range_type": "last_7_days"})
        response = self.client.get(reverse("analytics_api"), {"range_type": "last_7_days"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response_time", response.json())
