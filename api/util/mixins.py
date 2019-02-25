from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

from api.models import Token


class ValidateToken(AccessMixin, ContextMixin):
    permission_denied_message = 'Acceso no permitido'
    no_token_message = 'El token no existe en la consulta'
    token_request = ''

    def handle_no_token(self):
        raise KeyError(self.no_token_message)

    def handle_no_permission(self):
        raise PermissionDenied(self.permission_denied_message)

    def dispatch(self, request, *args, **kwargs):
        if 'token' in request.GET:
            self.token_request = request.GET['token']
        else:
            return self.handle_no_token()
        try:
            Token.objects.get(token=self.token_request)
            return super().dispatch(request, *args, **kwargs)
        except Token.DoesNotExist:
            return self.handle_no_permission()
