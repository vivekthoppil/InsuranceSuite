from django.conf.urls import url

from .controllers import LoginController, RegistrationController

app_name = 'authentication'

urlpatterns = [
    url(r'^users/?$', RegistrationController.as_view(),
        name='user-registration'),
    url(r'^users/login/?$', LoginController.as_view(), name='user-login'),
]
