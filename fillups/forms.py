from django import forms

class FillupForm(forms.ModelForm):

    class Meta():
        model = Fillup
        fields = ('date', 'price_per_gallon', 'trip_distance', 'gallons', 'total_sale', 'car')


class CarForm(forms.ModelForm):

    class Meta():
        model = Car
        fields = ('name', 'make', 'model', 'model_year', 'status')
