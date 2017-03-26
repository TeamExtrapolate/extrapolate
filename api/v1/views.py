import os

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from SIH17.authentication import CustomTokenAuthentication
from analysis.forms import AnalysisTestForm
from analysis.script import execute
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

    def post(self, request, *args, **kwargs):
        return Response({"hello": 1})


@require_POST
@csrf_exempt
def analysis_post(request):
    f = AnalysisTestForm(request.POST, request.FILES)
    if f.is_valid():
        obj = f.save()
        path = execute(obj.test_file.name)
        if os.path.exists(path):
            with open(path, 'rb') as fh:
                response = HttpResponse(fh.read(),
                                        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
                return response
    return JsonResponse(data={'status': 'Success'}, status=200)
