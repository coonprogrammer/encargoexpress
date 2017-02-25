from sqlalchemy import event

from encargoapi import app, db


class Journal(db.Model):

    __tablename__ = 'journal'

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    table_name = db.Column(db.String, index=True, nullable=False)
    field_name = db.Column(db.String, index=True, nullable=False)
    new_value = db.Column(db.String, nullable=False)
