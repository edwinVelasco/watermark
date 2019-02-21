import hashlib
import datetime
from django.core.management.base import BaseCommand
from api.models import Token


class Command(BaseCommand):
    help = 'Create token'
    api_key = '76634530ffcbfd1ed0e621e59b59b887'

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        string = f"{self.api_key}{now.strftime('%Y%m%d')}"
        new_token = hashlib.md5(string.encode('utf-8'))
        try:
            token = Token()
            token.token = new_token.hexdigest()
            token.save()
            Token.objects.exclude(id=token.id).delete()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully registered token, '
                                   f'{new_token.hexdigest()}')
            )
        except Exception as error:
            print(error)
            self.stderr.write(f'hopeless registered token, '
                              f'{new_token.hexdigest()}')
