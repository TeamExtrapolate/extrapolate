import os
import uuid

from django.http import HttpResponse
from django.views.generic.edit import FormView

from analysis.forms import AnalysisTestForm
from analysis.script import execute
from api.tasks import upload_s3


class PredictionsView(FormView):
    template_name = 'employment.html'
    form_class = AnalysisTestForm

    def form_valid(self, form):
        file = self.request.FILES['test_file']
        old_path = 'tmp/tests/%s.xlsx' % uuid.uuid4()
        with open(old_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        path = execute(old_path)
        upload_s3.apply_async([old_path, path], queue='uploads', routing_key='s3.uploads')
        if os.path.exists(path):
            with open(path, 'rb') as fh:
                response = HttpResponse(fh.read(),
                                        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
                return response
