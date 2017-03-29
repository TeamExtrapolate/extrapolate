import magic
from django import forms

from .models import AnalysisTest


class AnalysisTestForm(forms.ModelForm):
    class Meta:
        model = AnalysisTest
        fields = '__all__'

    def get_test_file(self):
        return self.cleaned_data.get('test_file').name
