import os
import unittest
import argparse
import time
from random import uniform, choice

from docopt import docopt
from flask_script import Manager

from encargoapi import app, db
from encargoapi.billing.model import Invoice
from encargoapi.client.model import Client


manager = Manager(app)


@manager.command
def drop_and_create_databases():
    db.session.remove()
    db.reflect()
    db.drop_all()
    db.create_all()


@manager.command
def create_fake_invoices(client_id=False, **kwargs):
    if not client_id:
        client = Client(
            name='Client Nicolas',
            type_id=1,
            identifier='20329757782',
            identifier_type_id=3,
            contact='',
            address='Address',
            phone='123123123',
        )
        db.session.add(client)
        db.session.commit()
    else:
        client = Client.query.filter_by(id=client_id).first()

    for i in range(10000):
        total = round(uniform(-1, 1) * 10, 2)
        iva =  choice([4, 10.5, 21, 24])
        iva_total = round(iva * total / 100, 2)
        gross = round(total - iva_total, 2)
        try:
            invoice = Invoice(
                client_id=client.id,
                client_name=client.name,
                client_address=client.address,
                client_identifier=client.identifier,
                client_identifier_type=client.identifier_type_id,
                ref_num=i,
                description="Description",
                iva=iva,
                iva_total=iva_total,
                net=kwargs.get('net',21),
                gross=gross,
                total=total,
                invoice_type_id=kwargs.get('invoice_type_id', 1),
                paid=0,
                paid_date=None,
                status=0,
            )
            db.session.add(invoice)
            db.session.commit()
        except Exception as e:
            print 'Ooops! {}'.format(e)
            raise


@manager.command
def drop_and_create_databases_and_fake_data():
    drop_and_create_databases()
    create_fake_invoices()


@manager.command
def tests():
    os.system('python -m unittest discover -v')


if __name__ == "__main__":
    manager.run()
