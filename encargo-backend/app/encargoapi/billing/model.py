from datetime import datetime
from flask import request
from sqlalchemy import event

from encargoapi import app, db
from encargoapi.client.model import Client
from encargoapi.database import ModelBase


class Invoice(ModelBase, db.Model):

    __tablename__ = 'billing'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    client_name = db.Column(db.String, nullable=False)
    client_address = db.Column(db.String, nullable=False)
    client_identifier = db.Column(db.String, nullable=False)
    client_identifier_type = db.Column(db.String, db.ForeignKey('client_identifier_type.id'), nullable=False)

    ref_num = db.Column(db.String, index=True, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    discount = db.Column(db.Float, nullable=True, default=0)
    taxable_base = db.Column(db.Float, nullable=False, default=0)
    iva = db.Column(db.Float, nullable=False)
    iva_total = db.Column(db.Float, nullable=False)
    net = db.Column(db.Float, nullable=False)
    gross = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    paid = db.Column(db.Boolean, default=0)
    paid_date = db.Column(db.DateTime, default=None)
    status = db.Column(db.Integer, db.ForeignKey('invoice_status.id'), default=0)

    invoice_type_id = db.Column(db.Integer, db.ForeignKey('invoice_type.id'))

    def create_new_invoice(self, client_id):
        import ipdb;ipdb.set_trace()


class InvoiceItem(ModelBase, db.Model):

    __tablename__ = 'invoice_item'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    code = db.Column(db.String, index=True)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    iva = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)


class InvoiceType(ModelBase, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    invoices = db.relationship(
        'Invoice',
        backref='invoice_type'
    )


@event.listens_for(InvoiceType.__table__, 'after_create')
def insert_initial_values_invoices_type(*args, **kwargs):
    db.session.add(InvoiceType(type='A'))
    db.session.add(InvoiceType(type='B'))
    db.session.add(InvoiceType(type='C'))
    db.session.commit()


class InvoiceStatus(ModelBase, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), nullable=False)
    status_code = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String, nullable=True)
    invoices = db.relationship(
        'Invoice',
        backref='invoice_status'
    )


@event.listens_for(InvoiceType.__table__, 'after_create')
def insert_initial_values_invoices_type(*args, **kwargs):
    db.session.add_all([
        InvoiceStatus(status_code='0', status='Created'),
        InvoiceStatus(status_code='10', status='Sent'),
        InvoiceStatus(status_code='20', status='Paid'),
        InvoiceStatus(status_code='100', status='Canceled'),
    ])
    db.session.commit()
