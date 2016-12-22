from flask import Flask

app = Flask(__name__)

from encargoapi import views
from encargoapi.auth import views
from encargoapi.billing import views
from encargoapi.user import views
from encargoapi.client import views
