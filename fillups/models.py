from django.db import models
from datetime import date, datetime

from django.contrib.auth import get_user_model
User = get_user_model()

next_year = datetime.today().year+1
last_30_years = list(range(next_year-30, next_year))
MODEL_YEARS = [(i,j) for i,j in zip(last_30_years,last_30_years)]

STATUS = [(True, 'Active'), (False, 'Inactive')]

# Create your models here.
class Fillup(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    price_per_gallon = models.FloatField()
    trip_distance = models.FloatField()
    gallons = models.FloatField()
    car = models.ForeignKey('Car',on_delete=models.CASCADE)

    @property
    def total_sale(self):
        return round(self.price_per_gallon*self.gallons, 2)

    @property
    def mpg(self):
        return round(self.trip_distance/self.gallons, 4)


class Car(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    model_year = models.IntegerField(choices=MODEL_YEARS)
    status = models.BooleanField(choices=STATUS)

    def __str__(self):
        return self.name
