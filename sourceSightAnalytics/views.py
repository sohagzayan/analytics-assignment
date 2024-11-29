from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .services import AnalyticsService

class AnalyticsAPI(APIView):
    def get(self, request):
        range_type = request.query_params.get("range_type", "last_7_days")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        # Validate input
        if range_type == "custom" and (not start_date or not end_date):
            raise ValidationError("Custom range requires 'start_date' and 'end_date'.")

        # Use the service to get analytics
        service = AnalyticsService()
        result = service.get_analytics(range_type, start_date, end_date)

        return Response(result)
