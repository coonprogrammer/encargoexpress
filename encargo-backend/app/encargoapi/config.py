from encargoapi import app

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/encargoexpress.db'
db = SQLAlchemy(app)