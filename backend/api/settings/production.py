from api.settings.base import * # noqa

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

# separated by space
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", '').split(" ")

CORS_ORIGIN_WHITELIST = os.environ.get("DJANGO_CORS_ORIGIN_WHITELIST", '').split(" ")

USE_X_FORWARDED_HOST = True
