import json
import pandas as pd
from tcg.services.insert import insert_values
from tcg.services.search import search_card, search_in_cache
from functions_framework import http
from flask import jsonify

@http
def get(req):
    try:
        data = req.get_json(silent=True)
        if not data:
            return jsonify(dict(status=400,
                                message='Invalid or missing JSON')), 400

        cache_rs = search_in_cache(cat=data.get('category'),
                                   key=data.get('code'))

        if cache_rs:
            json_str = cache_rs.get('json_data')
            data = json.loads(json_str)
            df = pd.DataFrame(data)
            result = insert_values(df)
        else:
            result = search_card(category=data.get('category'),
                             key=data.get('code'))

        return jsonify(dict(status=result.get('status'),
                            message=result.get('message')))

    except Exception as e:
        return jsonify(dict(status=500,
                            message=f'Error {e}')), 500

