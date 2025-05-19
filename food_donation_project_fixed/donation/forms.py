from django import forms
from .models import FoodReport

class FoodReportForm(forms.ModelForm):
    class Meta:
        model = FoodReport
        fields = ['location', 'quantity']
