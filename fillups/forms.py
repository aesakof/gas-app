from django import forms
from .models import Fillup, Car

class FillupForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(FillupForm,self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(username=user)

    class Meta():
        model = Fillup
        fields = ('date', 'price_per_gallon', 'trip_distance', 'gallons', 'car')


class CarForm(forms.ModelForm):

    class Meta():
        model = Car
        fields = ('name', 'make', 'model', 'model_year', 'status')
