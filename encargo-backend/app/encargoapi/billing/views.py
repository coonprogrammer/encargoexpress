from flask import (
    jsonify,
    request,
    g,
)

from encargoapi import app
from encargoapi.auth import auth
from encargoapi.billing.model import Invoice
from encargoapi.client.model import Client

# curl -i -H "Content-type: application/json" http://localhost:5000/api/v1.0/invoicestest -d '{"user_id":"1"}' -X GET
@app.route('/api/v1.0/invoicestest/<int:client_id>', methods=['GET'])
def get_invoices_by_client_id(client_id):
    client = Client.query.filter_by(id=client_id).first()
    import ipdb;ipdb.set_trace()


@app.route('/api/v1.0/invoices', methods=['GET'])
@auth.login_required
def get_invoices():
    return jsonify({'invoices': '3'})


@app.route('/api/v1.0/invoices', methods=['POST'])
@auth.login_required
def create_invoice():
    pass


@app.route('/api/v1.0/invoice/<int:invoice_id>', methods=['PUT'])
@auth.login_required
def modify_invoice(invoice_id):
    pass


@app.route('/api/v1.0/invoice/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    pass