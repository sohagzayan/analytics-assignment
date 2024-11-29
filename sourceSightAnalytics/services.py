from datetime import timedelta, date
from collections import defaultdict
from django.db.models import Sum
from django.core.cache import cache
import time
from .models import Visitor

class AnalyticsService:
    def __init__(self):
        self.date_source_map = defaultdict(lambda: {"facebook": 0, "google": 0, "instagram": 0})

    def get_date_range(self, range_type, start_date=None, end_date=None):
        if range_type == "last_7_days":
            end_date = date.today()
            start_date = end_date - timedelta(days=7)
        elif range_type == "last_30_days":
            end_date = date.today()
            start_date = end_date - timedelta(days=30)
        elif range_type == "custom" and start_date and end_date:
            start_date = start_date
            end_date = end_date
        else:
            raise ValueError("Invalid range_type or missing dates.")
        return start_date, end_date

    def fetch_visitor_data(self, start_date, end_date):
        query = Visitor.objects.filter(date__range=(start_date, end_date))
        aggregated_data = query.values("date", "source").annotate(total=Sum("count"))
        return aggregated_data

    def format_response(self, aggregated_data):
        for record in aggregated_data:
            self.date_source_map[record["date"]][record["source"]] = record["total"]

        response = []
        for date, sources in self.date_source_map.items():
            response.append({
                "date": date,
                "sources": sources,
            })
        return response

    def get_cached_response(self, cache_key):
        return cache.get(cache_key)

    def set_cached_response(self, cache_key, data, timeout=300):
        cache.set(cache_key, data, timeout)

    def get_analytics(self, range_type, start_date=None, end_date=None):
        start_time = time.time()

        # Step 1: Determine Cache Key
        cache_key = f"analytics_{range_type}_{start_date}_{end_date}"
        cached_response = self.get_cached_response(cache_key)
        if cached_response:
            return {"data": cached_response, "response_time": f"{(time.time() - start_time):.2f} ms"}

        # Step 2: Process Request
        start_date, end_date = self.get_date_range(range_type, start_date, end_date)
        aggregated_data = self.fetch_visitor_data(start_date, end_date)
        response_data = self.format_response(aggregated_data)

        # Step 3: Cache Response
        self.set_cached_response(cache_key, response_data)

        end_time = time.time()
        return {"data": response_data, "response_time": f"{(end_time - start_time):.2f} ms"}
