from rest_framework.authentication import TokenAuthentication

from auth_token.models import AuthToken


class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'AuthToken'
    model = AuthToken
