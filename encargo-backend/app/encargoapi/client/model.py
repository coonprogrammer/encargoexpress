import json
from sqlalchemy import event

from encargoapi import app, db
from encargoapi.database import ModelBase


class Client(ModelBase, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(
        db.Integer,
        db.ForeignKey('client_type.id'),
        index=True,
        nullable=False,
    )
    name = db.Column(db.String, index=True, nullable=False)
    identifier = db.Column(db.String, index=True, nullable=False, unique=True)
    identifier_type_id = db.Column(
        db.Integer,
        db.ForeignKey('client_identifier_type.id'),
        index=True,
        nullable=False,
    )
    contact = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, index=True, nullable=True)


@event.listens_for(Client.__table__, 'after_create')
def insert_initial_values_client(*args, **kwargs):
    client = Client(
        type_id=1,
        name='Cliente Prueba',
        identifier='32323232',
        identifier_type_id=2,
        contact='',
        address='B Razquin 2899',
        phone='3163412',
    )
    db.session.add(client)
    db.session.commit()


class ClientType(ModelBase, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    code = db.Column(db.String(5), index=True, nullable=False)
    description = db.Column(db.String, nullable=True)
    clients = db.relationship(
        'Client',
        backref='type'
    )


@event.listens_for(ClientType.__table__, 'after_create')
def insert_initial_values_client_type(*args, **kwargs):
    db.session.add_all([
        ClientType(label='Consumidor Final', code='CF'),
        ClientType(label='Responsable Inscripto', code='RI'),
    ])
    db.session.commit()


class ClientIdentifierType(ModelBase, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    clients = db.relationship(
        "Client",
        backref='identifier_type',
    )


@event.listens_for(ClientIdentifierType.__table__, 'after_create')
def insert_initial_values_client_identifier_type(*args, **kwargs):
    db.session.add_all([
        ClientIdentifierType(label='CUIT'),
        ClientIdentifierType(label='CUIL'),
        ClientIdentifierType(label='DNI'),
        ClientIdentifierType(label='Libreta de Enrolamiento'),
        ClientIdentifierType(label='Pasaporte'),
    ])
    db.session.commit()

