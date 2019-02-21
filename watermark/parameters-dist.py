# Database config
PG_DBNAME = ''

# Project config
DJ_SECRET_KEY = ''
DJ_DEBUG = False
DJ_ALLOWED_HOSTS = ['*']
DJ_LANGUAGE_CODE = 'es-co'
DJ_TIME_ZONE = 'America/Bogota'
DJ_USE_I18N = False
DJ_USE_L10N = True
DJ_USE_TZ = False
'''
test-software@udes.edu.co
Udes2018*
'''
# Email config
DJ_EMAIL_HOST = 'smtp.office365.com'
DJ_EMAIL_PORT = 587
DJ_EMAIL_HOST_USER = 'test-software@udes.edu.co'
DJ_EMAIL_HOST_PASSWORD = 'Udes2018*'

DJ_EMAIL_USE_TLS = True
DJ_DEFAULT_FROM_EMAIL = 'noreply-VAF UDES<test-software@udes.edu.co>'
DJ_SERVER_EMAIL = 'test-software@udes.edu.co'

DJ_SEND_TO_EMAIL = ''

CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = '6379'

ACCESS_TOKEN_DROPBOX = ''