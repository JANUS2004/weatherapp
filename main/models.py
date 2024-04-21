from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    lon = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    pressure = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    visibility = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather in {self.city}, {self.country_code}"



