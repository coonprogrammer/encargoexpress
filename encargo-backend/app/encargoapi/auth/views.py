from flask import (
    jsonify,
    request,
    g,
)

from . import auth
from encargoapi import app
from encargoapi.user.model import User

@app.route('/api/v1.0/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })


@app.route('/api/v1.0/token/check')
@auth.login_required
def check_auth_token():
    token = User.verify_auth_token(request.json.get('token'))
    return jsonify({ 'token': token.decode('ascii') })
