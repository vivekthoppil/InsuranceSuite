from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.db import IntegrityError

from api.core.exceptions import AmbiguityException, ObjectAlreadyExists
from api.core.utils import generate_jwt_token

from .models import User


def create_user(username, password, email, **kwargs):
    if not all([username, password, email]):
        raise ImproperlyConfigured('Must provide username, password\
                                   and email for user')
    try:
        user = User.objects.create_user(username, email, password, **kwargs)
    except IntegrityError:
        raise ObjectAlreadyExists('User already exists')
    return user


def create_user_token(email, password):
    try:
        user = User.objects.get(email=email, password=password)
    except User.DoesNotExist:
        raise ObjectDoesNotExist('No user found')
    except User.MultipleObjectsReturned:
        raise AmbiguityException('Multiple users found with the same \
                                        credentials')

    user_info = {
        'email': user.email,
        'username': user.username
    }

    token = generate_jwt_token(user_info)
    return token
