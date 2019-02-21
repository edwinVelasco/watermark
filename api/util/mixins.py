from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from api.models import Token


class ValidateToken(AccessMixin, ContextMixin):
    permission_denied_message = 'Acceso no permitido'
    no_token_message = 'El token no existe en la consulta'
    token_request = ''
    token = None

    def handle_no_token(self):
        print('handle_no_token')
        raise KeyError(self.no_token_message)

    def handle_no_permission(self):
        print('handle_no_permission')
        raise PermissionDenied(self.permission_denied_message)

    def get_context_data(self, **kwargs):
        print('get_context_data')
        print(kwargs)
        context = super(ValidateToken, self).get_context_data(**kwargs)
        context['token'] = self.token
        return context

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        print('kwargs', kwargs)
        print('args', args)
        if request.method == 'GET' and 'token' in request.GET:
            self.token_request = self.request.GET('token')
        elif request.method == 'POST' and 'token' in request.POST:
            self.token_request = self.request.GET('token')
        else:
            return self.handle_no_token()
        try:
            token = Token.objects.get(token=self.token_request)
            return self.get_context_data(**kwargs)
        except Token.DoesNotExist:
            return self.handle_no_permission()
