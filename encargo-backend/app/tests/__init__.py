import unittest

from encargoapi import app
from encargoapi.config import db


class TestBase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config.update(
            DEBUG=True,
            TESTING=True,
            SQLALCHEMY_DATABASE_URI="sqlite:////tmp/encargoexpress_test.db",
        )
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
