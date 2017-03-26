import magic
from django import forms

from .models import AnalysisTest


class AnalysisTestForm(forms.ModelForm):
    class Meta:
        model = AnalysisTest
        fields = '__all__'

    def clean_test_file(self):
        file = self.cleaned_data.get("test_file", None)
        if file:
            mime = magic.from_buffer(file.read(), mime=True)
            if mime != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                raise forms.ValidationError('Invalid file format')
        return file
