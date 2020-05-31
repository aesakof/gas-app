from django.db import models
from datetime import date, datetime

next_year = datetime.today().year+1
last_30_years = list(range(next_year-30, next_year))
MODEL_YEARS = [(i,j) for i,j in zip(last_30_years,last_30_years)]

STATUS = [(True, 'Active'), (False, 'Inactive')]

# Create your models here.
class Fillup(models.Model):
    date = models.DateField(default=date.today)
    price_per_gallon = models.FloatField()
    trip_distance = models.FloatField()
    gallons = models.FloatField()
    total_sale = models.FloatField()
    mpg = models.FloatField()
    car = models.ForeignKey('Car',on_delete=models.CASCADE)

    @property
    def test_mpg(self):
        return self.trip_distance/self.gallons


class Car(models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    model_year = models.IntegerField(choices=MODEL_YEARS)
    status = models.BooleanField(choices=STATUS)

    def __str__(self):
        return self.name
