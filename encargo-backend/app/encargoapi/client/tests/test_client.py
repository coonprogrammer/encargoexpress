import json
import base64

from tests import TestBase
from encargoapi.client.model import Client


class TestClient(TestBase):

    def setUp(self):
        super(TestClient, self).setUp()

        self.data_clients_mock = [
            {
                u'name': u'nicolas',
                u'identifier': u'32975778',
                u'address': u'B Razquin 2899',
                u'client_type': 2,
                u'phone': u'4321',
                u'contact': u'',
            },
            {
                u'name': u'nicolas 2',
                u'identifier': u'12312312',
                u'address': u'Guillermo Molina 267 Dorrego Guaymallen',
                u'client_type': 1,
                u'phone': u'1234',
                u'contact': u'',
            },
        ]

        self.data_user_mock = {
            u'username': u'nicolas',
            u'password': u'password',
        }
        response = self.app.post(
            '/api/v1.0/users',
            data=json.dumps(self.data_user_mock),
            headers={"content-type": "application/json"},
        )
        self.user = json.loads(response.data)

    def test_client_save_and_get(self):
        # SAVE NEW CLIENT
        for client in self.data_clients_mock:
            response = self.app.post(
                '/api/v1.0/clients',
                data=json.dumps(client),
                headers={
                    'content-type': 'application/json',
                    'Authorization': 'Basic {}'.format(
                        base64.b64encode(
                            '{username}:{password}'.format(
                                username=self.data_user_mock['username'],
                                password=self.data_user_mock['password'],
                            )
                        )
                    ),
                },
            )
            self.assertEqual(response.status_code, 201)

        response_data = json.loads(response.data)
        new_data_clients_mock = self.data_clients_mock[1].copy()
        new_data_clients_mock.update({u'id':2})
        self.assertEqual(
            response_data,
            new_data_clients_mock,
        )

        # GET CLIENTS
        response = self.app.get(
            '/api/v1.0/clients',
            headers={
                'content-type': 'application/json',
                'Authorization': 'Basic {}'.format(
                    base64.b64encode(
                        '{username}:{password}'.format(
                            username=self.data_user_mock['username'],
                            password=self.data_user_mock['password'],
                        )
                    )
                ),
            },
        )

        clients = json.loads(response.data)
        new_data_clients_mock = list(self.data_clients_mock)
        for i in range(len(new_data_clients_mock)):
            new_data_clients_mock[i].update({u'id':i+1})

        self.assertEqual(len(clients), len(new_data_clients_mock))
        self.assertEqual(clients, new_data_clients_mock)

        # GET A CLIENT
        response = self.app.get(
            '/api/v1.0/client/1',
            headers={
                'content-type': 'application/json',
                'Authorization': 'Basic {}'.format(
                    base64.b64encode(
                        '{username}:{password}'.format(
                            username=self.data_user_mock['username'],
                            password=self.data_user_mock['password'],
                        )
                    )
                ),
            },
        )
        client = json.loads(response.data)
        new_data_client_mock = list(self.data_clients_mock)
        new_data_client_mock[0].update({u'id':1})
        self.assertEqual(client, new_data_client_mock[0])
