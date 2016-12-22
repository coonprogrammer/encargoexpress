from encargoapi import app
from encargoapi.config import db


class Invoices(db.Model):

    __tablename__ = 'billing'

    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.Datetime, nullable=False)
    invoiceType = db.Column(db.Integer)

    # friendsR = db.relationship('friendships', backref='friendships.friend_id', primaryjoin='users.id==friendships.user_id', lazy='joined')

class InvoicesType(db.Model):

    __tablename__ = 'invoices_type'

    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.Datetime, nullable=False)
