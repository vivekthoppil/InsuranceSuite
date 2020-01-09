import json

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from api.apps.authentication.models import User


class TestRegistrationController(APITestCase):

    def test_user_registration_success(self):
        response = self.client.post(
            reverse('authentication:user-registration'),
            json.dumps(
                {
                    'user': {
                        'username': 'johndoe',
                        'password': '12345678',
                        'email': 'johndoe@gmail.com'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.data.get('username'))
        self.assertIsNotNone(response.data.get('email'))
        self.assertIsNotNone(response.data.get('token'))

    def test_malformed_request_data_unsuccesful(self):
        response = self.client.post(
            reverse('authentication:user-registration'),
            json.dumps(
                {

                    'username': 'johndoe',
                    'password': '12345678',
                    'email': 'johndoe@gmail.com'

                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)
        self.assertTrue('error' in response.data['errors'])
        ed = response.data['errors']['error'][0]
        self.assertEqual(ed.lower(), 'no data provided')

    def test_invalid_emails(self):
        response = self.client.post(
            reverse('authentication:user-registration'),
            json.dumps(
                {
                    'user': {
                        'username': 'johndoe',
                        'password': '12345678',
                        'email': 'johnmail.com'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)
        self.assertTrue('email' in response.data['errors'])
        ed = response.data['errors']['email'][0]
        self.assertEqual(ed.lower(), 'enter a valid email address.')

    def test_no_email_provided(self):
        response = self.client.post(
            reverse('authentication:user-registration'),
            json.dumps(
                {
                    'user': {
                        'username': 'johndoe',
                        'password': '12345678',
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)
        self.assertTrue('email' in response.data['errors'])
        ed = response.data['errors']['email'][0]
        self.assertEqual(ed.lower(), 'this field is required.')

    def test_no_password_provided(self):
        response = self.client.post(
            reverse('authentication:user-registration'),
            json.dumps(
                {
                    'user': {
                        'username': 'johndoe',
                        'email': 'johndoe@mail.com'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)
        self.assertTrue('password' in response.data['errors'])
        ed = response.data['errors']['password'][0]
        self.assertEqual(ed.lower(), 'this field is required.')

    def test_no_username_provided(self):
        response = self.client.post(
            reverse('authentication:user-registration'),
            json.dumps(
                {
                    'user': {
                        'email': 'johndoe@mail.com',
                        'password': '12345678'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)
        self.assertTrue('username' in response.data['errors'])
        ed = response.data['errors']['username'][0]
        self.assertEqual(ed.lower(), 'this field is required.')

    def test_user_already_exists(self):
        user = User(
            username='johndoe',
            email='johndoe@gmail.com',
            password='12345678'
        )
        user.save()
        response = self.client.post(
            reverse('authentication:user-registration'),
            json.dumps(
                {
                    'user': {
                        'username': 'johndoe',
                        'password': '12345678',
                        'email': 'johndoe@gmail.com'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(409, response.status_code)
        self.assertTrue('errors' in response.data)
        ed = response.data['errors']['detail']
        self.assertEqual(ed.lower(), 'user already exists')


class TestLoginController(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('johndoe', 'johndoe@gmail.com',
                                             '12345678')

    def test_invalid_credential_login(self):
        self.user.delete()
        response = self.client.post(
            reverse('authentication:user-login'),
            json.dumps(
                {
                    'user': {
                        'password': '12345678',
                        'email': 'johndoe@gmail.com'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(403, response.status_code)

    def test_login_sucess(self):
        response = self.client.post(
            reverse('authentication:user-login'),
            json.dumps(
                {
                    'user': {
                        'password': '12345678',
                        'email': 'johndoe@gmail.com'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.data.get('username'))
        self.assertIsNotNone(response.data.get('email'))
        self.assertIsNotNone(response.data.get('token'))

    def test_malformed_request_data_unsuccesful(self):
        response = self.client.post(
            reverse('authentication:user-login'),
            json.dumps(
                {
                    'password': '12345678',
                    'email': 'johndoe@gmail.com'

                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)

    def test_no_email_provided(self):
        response = self.client.post(
            reverse('authentication:user-login'),
            json.dumps(
                {
                    'user': {
                        'password': '12345678',
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)
        self.assertTrue('email' in response.data['errors'])
        ed = response.data['errors']['email'][0]
        self.assertEqual(ed.lower(), 'this field is required.')

    def test_no_password_provided(self):
        response = self.client.post(
            reverse('authentication:user-login'),
            json.dumps(
                {
                    'user': {
                        'email': 'johndoe@mail.com'
                    }
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response.data)
        self.assertTrue('password' in response.data['errors'])
        ed = response.data['errors']['password'][0]
        self.assertEqual(ed.lower(), 'this field is required.')
