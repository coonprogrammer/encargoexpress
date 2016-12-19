from flask import Flask

app = Flask(__name__)

from encargoapi import (
    config,
    routes,
)
from encargoapi.user import routes
