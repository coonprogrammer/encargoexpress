from encargoapi import app


@app.route('/api/v1.0/invoices', methods=['GET'])
def get_invoices():
    pass


@app.route('/api/v1.0/invoices', methods=['POST'])
def create_invoice():
    pass


@app.route('/api/v1.0/invoice/<int:invoice_id>', methods=['PUT'])
def modify_invoice(invoice_id):
    pass


@app.route('/api/v1.0/invoice/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    pass