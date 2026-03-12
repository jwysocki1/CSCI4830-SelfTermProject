from django import forms
from .models import Date, Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['time','name','calories','protein','fat','carbs']
    
    time = forms.TimeField()
    name = forms.CharField(max_length=50)
    calories = forms.IntegerField()
    protein = forms.IntegerField()
    fat = forms.IntegerField()
    carbs = form.IntegerField()