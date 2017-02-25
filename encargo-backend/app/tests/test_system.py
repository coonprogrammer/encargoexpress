import json

from . import TestBase

class TestSystem(TestBase):
    
    def test_system(self):
        response = self.app.get(
            '/testsystem',
            headers={'content-type': 'application/json'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'status': '1'})