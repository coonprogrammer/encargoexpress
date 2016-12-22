from encargoapi import app
from encargoapi.auth import auth
from encargoapi.config import db
from encargoapi.user.model import User

from flask import (
    abort,
    g,
    jsonify,
    request,
    url_for,
)

@app.route('/api/v1.0/users', methods = ['GET'])
def user():
    return jsonify({'users': 'ok'})

@app.route('/api/v1.0/users', methods = ['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify(
        {
            'id':user.id,
            'username':user.username,
        }
    ), 201, {'Location': url_for('get_user', user = user, _external = True)}


@app.route('/api/v1.0/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, {}!'.format(g.user.username) })


@app.route('/api/v1.0/user', methods=['GET'])
@auth.login_required
def get_user():
    return jsonify({
        'user': {
            'id': g.user.id,
            'username': g.user.username,
        }
    })
