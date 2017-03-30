import os

from celery import Celery
from django.core.files import File

from analysis.models import AnalysisTest

app = Celery('tasks')


@app.task(ignore_result=True)
def upload_s3(test_file, predicted_file):
    test_temp = open(test_file, 'rb')
    predicted_temp = open(predicted_file, 'rb')
    a = AnalysisTest(test_file=File(test_temp), predicted_file=File(predicted_temp))
    a.save()
    print(test_file, predicted_file)
    os.system('rm %s' % test_temp.name)
    os.system('rm %s' % predicted_temp.name)


@app.task
def hello():
    print(1)
