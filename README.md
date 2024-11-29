# 📊 SourceSight Analytics API

SourceSight Analytics is a Django-powered REST API for analyzing visitor data from various sources (Facebook, Google, Instagram) over custom date ranges. This API is optimized for performance, leveraging PostgreSQL for data aggregation and caching for speedy responses.

---

## 🚀 Features

- Retrieve visitor counts by date and source.
- Filter data for the last 7 days, 30 days, or custom date ranges.
- Optimized database queries for fast performance (under 100ms).
- Built-in caching to reduce repeated database queries.
- Modular and clean code adhering to Django best practices.

---

## 🛠️ Setup

1. **Clone the Repository**:

```bash
  git clone https://github.com/sohagzayan/analytics-assignment.git
   cd analytics-assignment
```

## Create a Virtual Environment:

```bash
   python -m venv venv
   source venv/bin/activate
```

## 🚀 Install Dependencies

```bash
   pip install -r requirements.txt
```

## 🚀 Set Up the Database

```bash
   python manage.py migrate
```

## 🚀 python manage.py migrate

```bash
   python manage.py runserver
```

## 🧪 ** API Endpoints **

- Retrieve Analytics Data
- URL: /api/analytics/
- Method: GET
- Query Parameters:
- range_type (string): last_30_days, last_7_days, or custom.
- start_date (optional, string): YYYY-MM-DD (required if range_type=custom).
- end_date (optional, string): YYYY-MM-DD (required if range_type=custom)

## 🚀 Example Request:

```bash
  GET http://127.0.0.1:8000/api/analytics/?range_type=last_7_days
```

## 🚀 Example Response:

```bash
 {
  "data": [
    {
      "date": "2023-11-01",
      "sources": {
        "facebook": 100,
        "google": 200,
        "instagram": 50
      }
    },
    {
      "date": "2023-11-02",
      "sources": {
        "facebook": 120,
        "google": 180,
        "instagram": 75
      }
    }
  ],
  "response_time": "50 ms"
}
```

## 🚀 Error Responses:

- Invalid range_type

```bash
  {
  "error": "Invalid range_type. Valid options are 'last_7_days', 'last_30_days', or 'custom'."
}
```

- Missing start_date or end_date for custom range:

```bash
  {
  "error": "Custom range requires 'start_date' and 'end_date'."
}
```

## 📝 ** Testing **

### Run automated tests for your API:

- Run Tests

```bash
 python manage.py test
```

- Test Coverage

- Includes:
  -- Valid and invalid query parameters.
  -- Cache hit/miss functionality.
  -- Response time validation.
