# This is a naive implementation of drf-yasg as i am learning.
# Can move to a better design once i get the hang of things.

from drf_yasg import openapi

user_schema_properties = {
    'username': {
        'type': 'string'
    },
    'password': {
        'type': 'string'
    },
    'email': {
        'type': 'string'
    }
}


UserSchema = openapi.Schema(title='User data', description='User info',
                            type='object',
                            properties=user_schema_properties,
                            required=['username', 'password', 'email'])

user_request_schema_properties = {
    'user': UserSchema,
}

user_request_example = {
    'user': {
        'username': 'johnsmith',
        'password': 'randompassword',
        'email': 'johnsmith@email.com'
    }
}

UserRequestSchema = openapi.Schema(title='User Request',
                                   description='User Request',
                                   type='object',
                                   properties=user_request_schema_properties,
                                   example=user_request_example)

###

user_response_properties = {
    'username': {
        'type': 'string'
    },
    'email': {
        'type': 'string'
    },
    'token': {
        'type': 'string'
    }
}


AuthorisedUserSchema = openapi.Schema(title='User data',
                                      description='User info',
                                      type='object',
                                      properties=user_response_properties,
                                      required=['username', 'password',
                                                'token'])

user_response_schema_properties = {
    'user': AuthorisedUserSchema,
}

user_response_example = {
    'user': {
        'username': 'johnsmith',
        'email': 'johnsmith@email.com',
        'token': 'xxxxx.yyyyy.zzzzz'
    },
    'errors': []
}

UserResponseSchema = openapi.Schema(title='User Response',
                                    description='User Response',
                                    type='object',
                                    properties=user_response_schema_properties,
                                    example=user_response_example)
###

login_request_properties = {
    'email': {
        'type': 'string'
    },
    'password': {
        'type': 'string'
    },
}


LoginSchema = openapi.Schema(title='Login data', description='Login data',
                             type='object',
                             properties=login_request_properties,
                             required=['password', 'email'])

login_request_schema_properties = {
    'user': LoginSchema,
}

login_request_example = {
    'user': {
        'email': 'johnsmith@email.com',
        'password': 'randompassword',
    }
}

LoginRequestSchema = openapi.Schema(title='User Request',
                                    description='User Request',
                                    type='object',
                                    properties=login_request_schema_properties,
                                    example=login_request_example)
