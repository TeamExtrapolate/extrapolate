# Copyright 2018 Team Extrapolate Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here
def change_test_file_name(instance, filename):
    extension = filename.split('.')[-1]
    filename = '%s.%s' % (
        int(datetime.datetime.now().strftime("%s")) * 1000, extension)
    path = 'file-uploads/tests/'
    return os.path.join(path, filename)


def change_predicted_file_name(instance, filename):
    extension = filename.split('.')[-1]
    filename = '%s.%s' % (
        int(datetime.datetime.now().strftime("%s")) * 1000, extension)
    path = 'file-uploads/prediction/'
    return os.path.join(path, filename)


class AnalysisTest(models.Model):
    test_file = models.FileField(
        upload_to=change_test_file_name, verbose_name='Analysis file')
    predicted_file = models.FileField(
        upload_to=change_predicted_file_name, verbose_name='Analysis predicted file')

    def __str__(self):
        return os.path.basename(self.test_file.name)

    # def clean(self):
    #     if self.test_file:
    #         mime = magic.from_buffer(self.test_file.read(), mime=True)
    #         if mime != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
    #             raise ValidationError('Invalid file format')
