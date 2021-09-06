from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Weather_Data(models.Model):
    temperature=models.IntegerField(
           validators=[MaxValueValidator(28), MinValueValidator(19)]
              )
    humidity=models.IntegerField(
           validators=[MaxValueValidator(65), MinValueValidator(35)]
              )
    date_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'The Temperature is {} and The Humidity {} on {}'.format(
                                            self.temperature,
                                              self.humidity,
                                              self.date_time
                                              )


class Summary_Data(models.Model):
    average_temperature=models.FloatField()
    averge_humidity=models.FloatField()
    start_date=models.DateTimeField(auto_now=False)
    end_date=models.DateTimeField(auto_now=False)
    def delete(self, *args, **kwargs):
        related_weather_data=Weather_Data.objects.filter(
                           date_time__gte=self.start_date
                           ).filter(
                           date_time__lte=self.end_date
                           )
        [data.delete() for data in related_weather_data]
        super(Summary_Data, self).delete(*args, **kwargs)

    def __str__(self):
        return 'The Average Temperature is {} and The Average Humidity {}'.format(
                                            self.average_temperature,
                                             self.averge_humidity,
                                              )        
