from flask import (
    jsonify,
    make_response,
)

from encargoapi import app

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.route('/testsystem')
def test_system():
    return make_response(jsonify({'status': '1'}), 200)