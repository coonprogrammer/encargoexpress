from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from encargoapi import views
from encargoapi.auth import views
from encargoapi.billing import views
from encargoapi.user import views
from encargoapi.client import views
