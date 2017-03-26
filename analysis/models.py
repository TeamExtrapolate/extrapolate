import datetime
import os

import magic
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def change_file_name(instance, filename):
    extension = filename.split('.')[-1]
    filename = '%s.%s' % (int(datetime.datetime.now().strftime("%s")) * 1000, extension)
    return '/'.join(['media', 'analysis', filename])


class AnalysisTest(models.Model):
    test_file = models.FileField(upload_to=change_file_name, verbose_name='Analysis file')

    def __str__(self):
        return os.path.basename(self.test_file.name)

    def clean(self):
        mime = magic.from_buffer(self.test_file.read(), mime=True)
        if mime != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            raise ValidationError('Invalid file format')
