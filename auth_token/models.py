import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token


# Create your models here.
class AuthToken(Token):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(_("Key"), max_length=40)
