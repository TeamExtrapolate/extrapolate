from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

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
