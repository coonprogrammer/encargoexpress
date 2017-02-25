from itsdangerous import (
    BadSignature,
    SignatureExpired,
    TimedJSONWebSignatureSerializer as Serializer,
)
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import event

from encargoapi import app, db
from encargoapi.database import ModelBase


class User(ModelBase, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    birthday = db.Column(db.Date, nullable=True)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


@event.listens_for(User.__table__, 'after_create')
def insert_initial_values_users(*args, **kwargs):
    if not app.config['TESTING']:
        user = User(username='admin')
        user.hash_password('admin')
        db.session.add(user)
        db.session.commit()