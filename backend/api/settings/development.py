from api.settings.base import * # noqa

# separated by space
ALLOWED_HOSTS = ('0.0.0.0', '127.0.0.1')

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://0.0.0.0:3000',
)
