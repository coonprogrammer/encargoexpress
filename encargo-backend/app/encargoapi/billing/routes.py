from encargoapi import app


@app.routes('/api/v1.0/receipts', methods=['GET'])
def get_receipts():
    pass


@app.routes('/api/v1.0/receipts', methods=['POST'])
def create_receipt():
    pass


@app.routes('/api/v1.0/receipt/<int: receipt_id>', methods=['PUT'])
def modify_receipt(receipt_id):
    pass


@app.routes('/api/v1.0/receipt/<int: receipt_id>', methods=['DELETE'])
def delete_receipt(receipt_id):
    pass