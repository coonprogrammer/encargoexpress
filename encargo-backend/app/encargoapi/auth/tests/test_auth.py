import json
import base64

from tests import TestBase


class TestAuth(TestBase):

    def setUp(self):
        super(TestAuth, self).setUp()

        self.data_user = {
            'username': 'nicolas',
            'password': 'password',
        }

    def test_auth(self):
        
        self.app.post(
            '/api/v1.0/users',
            data=json.dumps(self.data_user),
            headers={"content-type": "application/json"},
        )
        response = self.app.get(
            '/api/v1.0/token',
            data=json.dumps(self.data_user),
            headers={
                'content-type': 'application/json',
                'Authorization':'Basic {}'.format(
                    base64.b64encode(
                        '{username}:{password}'.format(
                            username=self.data_user['username'],
                            password=self.data_user['password'],
                        )
                    )
                )
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        response_data = json.loads(response.data)
        token = response_data['token']
        response = self.app.get(
            '/api/v1.0/token/check',
            headers={
                'content-type': 'application/json',
                'Authorization':'Basic {}'.format(
                    base64.b64encode(
                        '{username}:noused'.format(username=token)
                    )
                )
            }
        )
