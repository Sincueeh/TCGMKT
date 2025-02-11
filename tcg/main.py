import json
from tcg.services.search import search_card
from functions_framework import http
from flask import jsonify

@http
def get(req):
    try:
        data = req.get_json(silent=True)
        if not data:
            return jsonify(dict(status=400, message='Invalid or missing JSON')), 400

        search_card(category=data.get('category'), key=data.get('code'))
        return jsonify(dict(status=200, message='Success'))
    except Exception as e:
        return jsonify(dict(status=500, message=f'Error {e}')), 500
