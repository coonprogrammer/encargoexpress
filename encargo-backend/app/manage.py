import unittest
from flask_script import Manager

from encargoapi import app
from encargoapi.config import db


manager = Manager(app)


@manager.command
def create_databases():
    db.create_all()


@manager.command
def tests():
    unittest.main()


if __name__ == "__main__":
    manager.run()
