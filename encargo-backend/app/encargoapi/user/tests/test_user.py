import json
import base64

from tests import TestBase
from encargoapi.user.model import User


class TestUser(TestBase):

    def setUp(self):
        super(TestUser, self).setUp()
        self.data_user_mock = {
            'username': 'nicolas',
            'password': 'password',
        }

    def test_user(self):
        response = self.app.get(
            '/api/v1.0/users',
            headers={'content-type': 'application/json'},
        )
        self.assertEqual(
            response.status_code,
            200,
            'Status should be 200',
        )

        data = json.loads(response.data)
        self.assertEqual(
            data,
            {'users': 'ok'},
        )

    def test_create_user(self):
        
        response = self.app.post(
            '/api/v1.0/users',
            data=json.dumps(self.data_user_mock),
            headers={'content-type': 'application/json'},
        )
        self.assertEqual(response.status_code, 201)

        users = User.query.all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.data_user_mock['username'])

    def test_get_user(self):
        response_mock = {
            'user': {
                'id': 1,
                'username': self.data_user_mock['username'],
            }
        }

        # CREATE NEW USER
        self.app.post(
            '/api/v1.0/users',
            data=json.dumps(self.data_user_mock),
            headers={'content-type': 'application/json'},
        )

        response = self.app.get(
            '/api/v1.0/user',
            headers={
                'content-type': 'application/json',
                'Authorization':'Basic {}'.format(
                    base64.b64encode(
                        '{username}:{password}'.format(
                            username=self.data_user_mock['username'],
                            password=self.data_user_mock['password'],
                        )
                    )
                )
            },
        )
        self.assertEqual(
            json.loads(response.data),
            response_mock,
        )
