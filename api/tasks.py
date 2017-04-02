import os
from django.core.mail import EmailMultiAlternatives
from celery import Celery
from django.core.files import File
from celery.utils.log import get_task_logger
from django.core.mail import BadHeaderError
from django.conf import settings
import requests

logger = get_task_logger(__name__)
from analysis.models import AnalysisTest

app = Celery('tasks')


@app.task(ignore_result=True, bind=True)
def upload_s3(self, test_file, predicted_file, email):
    try:
        test_temp = open(test_file, 'rb')
        predicted_temp = open(predicted_file, 'rb')
        r = requests.post(settings.MAIL_GUN_API_DOMAIN, auth=("api", settings.API_KEY),
                          data={"from": settings.EMAIL_HOST_USER, "to": [email], "text": "Hi, here are your files",
                                "subject": "Team Extrapolate"},
                          files=[("attachment", ("test.xlsx", open(test_file, 'rb').read())),
                                 ("attachment", ("predicted.xlsx", open(predicted_file, 'rb').read()))])
        a = AnalysisTest(test_file=File(test_temp), predicted_file=File(predicted_temp))
        a.save()
        os.system('rm %s' % test_temp.name)
        os.system('rm %s' % predicted_temp.name)
        return a.id
    except Exception as e:
        self.retry(exc=e, countdown=60)


@app.task(ignore_result=True, bind=True)
def send_mail(self, test_file, predicted_file):
    try:
        subject, from_email, to = 'hello', settings.EMAIL_HOST, 'mailbag.akshay@gmail.com'
        text_content = 'This is an important message.'
        html_content = '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.attach_file(test_file)
        msg.attach_file(predicted_file)
        msg.send()
    except BadHeaderError:
        pass


@app.task
def hello():
    print(1)
