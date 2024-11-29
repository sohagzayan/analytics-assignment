from django.db import models

class Visitor(models.Model):
    DATE_CHOICES = [
        ("facebook", "Facebook"),
        ("google", "Google"),
        ("instagram", "Instagram"),
    ]
    date = models.DateField()
    source = models.CharField(max_length=50, choices=DATE_CHOICES)
    count = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=["date"]),
            models.Index(fields=["source"]),
        ]
