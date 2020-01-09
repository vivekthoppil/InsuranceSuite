from datetime import datetime, timedelta

import pytz
from django.conf import settings
from jose import jwt


def now():
    return datetime.now(pytz.utc)


def generate_jwt_token(user_info):
    token_expiration_time = now(
    ) + timedelta(seconds=int(settings.JWT_TOKEN_TIME_PERIOD_IN_SECONDS))
    jwt_payload = {
        'exp': token_expiration_time
    }
    jwt_payload.update(user_info)
    return jwt.encode(jwt_payload, settings.SECRET_KEY, algorithm='HS256')
