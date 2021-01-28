#!/usr/bin/python3
""" Flask web app """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """ Status of your API """
    return jsonify(status="OK")
