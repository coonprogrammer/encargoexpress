from encargoapi import app
from encargoapi.auth import auth
from encargoapi.config import db
from encargoapi.client.model import Client

from flask import (
    abort,
    g,
    jsonify,
    request,
    url_for,
)


@app.route('/api/v1.0/clients', methods=['POST'])
@auth.login_required
def create_client():
    name = request.json.get('name')
    address = request.json.get('address')
    client_type = request.json.get('client_type')
    client_identifier_type = request.json.get('client_identifier_type')
    identifier = request.json.get('identifier')
    phone = request.json.get('phone')
    contact = request.json.get('contact')

    if (
        client_type is None or
        client_identifier_type is None or
        address is None or
        name is None or
        identifier is None
    ):
        abort(400)  # missing arguments
    if Client.query.filter_by(identifier=identifier).first() is not None:
        abort(400)  # existing client

    client = Client(
        address=address,
        name=name,
        identifier=identifier,
        client_type=client_type,
        client_identifier_type=client_identifier_type,
        contact=contact,
        phone=phone,
    )
    db.session.add(client)
    db.session.commit()
    return jsonify(client.get_dict()), 201, {'Location': url_for('get_client', client_id=client.id, _external=True)}


@app.route('/api/v1.0/clients', methods=['GET'])
@auth.login_required
def get_clients():
    clients = Client.query.all()
    return jsonify([client.get_dict() for client in clients])


@app.route('/api/v1.0/client/<int:client_id>', methods=['GET'])
@auth.login_required
def get_client(client_id):
    client = Client.query.filter_by(id=client_id).first()
    return jsonify(client.get_dict())
