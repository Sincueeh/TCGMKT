import json
import pandas as pd
from tcg.services.insert import insert_values
from tcg.services.retrieve import get_sheets
from tcg.services.search import search_card, search_in_cache
from functions_framework import http
from flask import jsonify

@http
def get(req):
    try:
        data = req.get_json(silent=True)
        if not data:
            return jsonify({"status": 400, "message": "Invalid or missing JSON"}), 400

        # Buscar en la caché usando los parámetros "category" y "code"
        cache_rs = search_in_cache(cat=data.get('category'), key=data.get('code'))

        if cache_rs:
            # Extraemos el JSON almacenado (se asume que es una cadena)
            json_str = cache_rs.get('json_data')
            data_cache = json.loads(json_str)
            df = pd.DataFrame(data_cache)
            # Actualiza la hoja en caso de ser necesario y obtiene el resultado de la operación
            result = insert_values(df)

            count = len(df)
            cards = df.to_dict(orient='records')

            # Se añade el recuento al mensaje y se incluye el diccionario de resultados
            result['message'] = result.get('message', '') + f" Found {count} card{'s' if count != 1 else ''}."
            result['cards'] = cards
        else:
            # Si no hay registro en caché, se realiza la búsqueda en vivo
            result = search_card(category=data.get('category'), key=data.get('code'))
            # Suponiendo que search_card retorna un diccionario con una clave 'data'
            if 'data' in result and result['data'] is not None:
                cards = result['data']
                count = len(cards) if isinstance(cards, list) else 1
                result['message'] = result.get('message', '') + f" Found {count} card{'s' if count != 1 else ''}."
                result['cards'] = cards
            else:
                result['cards'] = []

        return jsonify({
            "status": result.get('status'),
            "message": result.get('message'),
            "cards": result.get('cards')
        })
    except Exception as e:
        return jsonify({"status": 500, "message": f"Error {e}"}), 500

@http
def get_results(req):
    try:
        worksheet = get_sheets()
        records = worksheet.get_all_records()

        return jsonify(records)

    except Exception as e:
        return jsonify({'status': 500, 'message': f'Error {e}'}), 500
