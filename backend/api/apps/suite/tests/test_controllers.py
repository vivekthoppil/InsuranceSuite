import time

from django.shortcuts import reverse
from django.test import override_settings
from rest_framework.test import APITestCase

from api.apps.authentication.models import User
from api.apps.authentication.services import create_user_token
from api.apps.suite.models import Attribute, AttributeType, RiskType


def create_attribute_types():
    attr = AttributeType(name='A1', description='Any text based data')
    attr.save()

    attr = AttributeType(name='A2', description='Any number based data')
    attr.save()

    attr = AttributeType(name='A3', description='Multiple Options')
    attr.save()

    attr = AttributeType(name='A4', description='Date data')
    attr.save()


def create_risk_types():
    create_risk_type('Commercial1',
                     'Insurance for Commercial properties')
    create_risk_type('Automobile1', 'Insurance for Automobile Vehicles')
    create_risk_type('Personal1', 'LIfe Insurance for persons')
    create_risk_type('HomeOwners1', 'Insurance for personal properties')


def create_risk_type(name, description):
    text_type = AttributeType.objects.filter(name='A1').first()
    num_type = AttributeType.objects.filter(name='A2').first()
    enum_type = AttributeType.objects.filter(name='A3').first()
    date_type = AttributeType.objects.filter(name='A4').first()

    r_type = RiskType(name=name, description=description)
    r_type.save()

    attr = Attribute(attribute_type=text_type, label='Name',
                     description='Name of Risk', risk_type=r_type,
                     required=True)
    attr.save()

    attr = Attribute(attribute_type=num_type, label='Age',
                     description='Age of Risk', risk_type=r_type,
                     required=True)
    attr.save()

    attr = Attribute(attribute_type=enum_type, label='Status',
                     description='Status of Risk', risk_type=r_type,
                     options='Valid,Invalid',
                     required=True)
    attr.save()

    attr = Attribute(attribute_type=date_type, label='Effective Date',
                     description='Coverage Start Date', risk_type=r_type,
                     required=True)
    attr.save()


class RiskTypeListController(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('johndoe', 'johndoe@gmail.com',
                                             '12345678')
        create_attribute_types()
        create_risk_types()

    def test_not_login(self):
        response = self.client.get(
            reverse('suite:list-risk-types'),
            content_type='application/json'
        )
        self.assertEqual(403, response.status_code)
        self.assertTrue('errors' in response.data)
        ed = response.data['errors']['detail']
        self.assertEqual(ed.lower(),
                         'authentication credentials were not provided.')

    def test_risk_types_list(self):
        self.user_token = create_user_token(self.user.email,
                                            self.user.password)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.get(
            reverse('suite:list-risk-types'),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.data['count'] > 0)

    @override_settings(JWT_TOKEN_TIME_PERIOD_IN_SECONDS=1)
    def test_token_expiry(self):
        self.user_token = create_user_token(self.user.email,
                                            self.user.password)
        time.sleep(2)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.get(
            reverse('suite:list-risk-types'),
            content_type='application/json'
        )
        self.assertEqual(403, response.status_code)
        self.assertTrue('errors' in response.data)
        ed = response.data['errors']['detail']
        self.assertEqual(ed.lower(),
                         'token has expired.')

    def test_token_format(self):
        self.user_token = 'abc'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.get(
            reverse('suite:list-risk-types'),
            content_type='application/json'
        )
        self.assertEqual(403, response.status_code)
        self.assertTrue('errors' in response.data)
        ed = response.data['errors']['detail']
        self.assertEqual(ed.lower(),
                         'invalid authentication. could not decode token.')


class RiskTypeDetailController(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('johndoe', 'johndoe@gmail.com',
                                             '12345678')
        create_attribute_types()
        create_risk_types()
        self.risk_type_id = RiskType.objects.get(name='Commercial1').id

    def test_not_login(self):
        response = self.client.get(
            reverse('suite:risk-type-detail',
                    kwargs={'risk_type_id': self.risk_type_id}),
            content_type='application/json'
        )
        self.assertEqual(403, response.status_code)
        self.assertTrue('errors' in response.data)
        ed = response.data['errors']['detail']
        self.assertEqual(ed.lower(),
                         'authentication credentials were not provided.')

    def test_risk_type_detail(self):
        self.user_token = create_user_token(self.user.email,
                                            self.user.password)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.get(
            reverse('suite:risk-type-detail',
                    kwargs={'risk_type_id': self.risk_type_id}),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)

    @override_settings(JWT_TOKEN_TIME_PERIOD_IN_SECONDS=1)
    def test_token_expiry(self):
        self.user_token = create_user_token(self.user.email,
                                            self.user.password)
        time.sleep(2)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.get(
            reverse('suite:risk-type-detail',
                    kwargs={'risk_type_id': self.risk_type_id}),
            content_type='application/json'
        )
        self.assertEqual(403, response.status_code)
        self.assertTrue('errors' in response.data)
        ed = response.data['errors']['detail']
        self.assertEqual(ed.lower(),
                         'token has expired.')

    def test_token_format(self):
        self.user_token = 'abc'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token)
        response = self.client.get(
            reverse('suite:risk-type-detail',
                    kwargs={'risk_type_id': self.risk_type_id}),
            content_type='application/json'
        )
        self.assertEqual(403, response.status_code)
        self.assertTrue('errors' in response.data)
        ed = response.data['errors']['detail']
        self.assertEqual(ed.lower(),
                         'invalid authentication. could not decode token.')
