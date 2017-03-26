import magic
from django import forms

from .models import AnalysisTest


class AnalysisTestForm(forms.ModelForm):
    class Meta:
        model = AnalysisTest
        fields = '__all__'
