from encargoapi import app

from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/encargoexpress.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'diacAQGacj432!#kuy(%&&"jl-fjkwhkc.anq3846t00[]*jak'