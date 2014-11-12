from django.conf import settings

CACHE_TIMEOUT = getattr(settings, 'DROPBOX_CACHE_TIMEOUT', 3600 * 24 * 365)   # One year
CONSUMER_KEY = getattr(settings, 'DROPBOX_CONSUMER_KEY', None)
CONSUMER_SECRET = getattr(settings, 'DROPBOX_CONSUMER_SECRET', None)
ACCESS_TOKEN = getattr(settings, 'DROPBOX_ACCESS_TOKEN', None)
ACCESS_TOKEN_SECRET = getattr(settings, 'DROPBOX_ACCESS_TOKEN_SECRET', None)

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = getattr(settings, 'DROPBOX_ACCESS_TYPE', 'dropbox')


