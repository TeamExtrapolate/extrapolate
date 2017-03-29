import boto3
from celery import Celery

app = Celery('tasks')


@app.task(ignore_result=True)
def upload_s3():
    s3 = boto3.resource('s3', aws_access_key_id='AKIAJKTS7B7S7TLFNL2Q',
                        aws_secret_access_key='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')
    data = open('media/analysis-results/result-1490815666000.xlsx', 'rb')
    a = s3.Bucket('sih17').put_object(Key='test.xlsx', Body=data)
    print(a)


@app.task
def hello():
    print(1)
