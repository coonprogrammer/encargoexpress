from sqlalchemy import event
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from encargoapi import db
from encargoapi.journal.model import Journal

class ModelBase(object):

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    def get_dict(self):
        return {
            item.key:self.__dict__[item.key] for item in self.__table__.columns.values()
        }

    def on_model_change(self, form, model, is_created=False):
        journal = Journal(
            table = self.__name__.lower(),
            field_name = '',
            new_value = '',
        )


# def my_before_commit(session):
#     import ipdb;ipdb.set_trace()
#     print "before commit!"

# Session = sessionmaker()

# event.listen(Session, "before_commit", my_before_commit)