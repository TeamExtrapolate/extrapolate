import uuid

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from SIH17.authentication import CustomTokenAuthentication
from analysis.forms import AnalysisTestForm
from analysis.script import execute
from api.tasks import upload_s3
from auth_token.models import AuthToken
from .token_gen import token_gen


# Create your views here.


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = AuthToken.objects.get_or_create(user=user)
        if not created:
            token.key = token_gen.generate_token()
            token.save()
        return Response({'token': token.key})


class TestLoginView(APIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        f = AnalysisTestForm(request.POST, request.FILES)
        print(f.is_valid())
        # print(f.errors.values())
        return Response({"hello": 1})


class PredictionAPIView(APIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    form_class = AnalysisTestForm

    def post(self, request):
        f = self.form_class(request.POST, request.FILES)
        if f.is_valid():
            file = request.FILES['test_file']
            old_path = 'tmp/tests/%s.xlsx' % uuid.uuid4()
            with open(old_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            path = execute(old_path)
            upload_s3.apply_async([old_path, path], queue='uploads', routing_key='s3.uploads')
            return Response({'message': 'Predictions file has been mailed to you.'}, status=200)
        else:
            return Response({'error': 'File was not valid'}, status=422)
