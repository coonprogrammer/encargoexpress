import json

from encargoapi import app
from encargoapi.config import db


class Client(db.Model):

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    client_type = db.Column(db.Integer, index=True, nullable=False)
    name = db.Column(db.String, index=True, nullable=False)
    identifier = db.Column(db.String, index=True, nullable=False)
    contact = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, index=True, nullable=True)

    def get_dict(self):
        return {
            'id': self.id,
            'client_type': self.client_type,
            'name': self.name,
            'identifier': self.identifier,
            'contact': self.contact,
            'address': self.address,
            'phone': self.phone,
        }


class ClientsType(db.Model):

    __tablename__ = 'clients_type'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
