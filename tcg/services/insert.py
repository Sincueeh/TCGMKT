import datetime
import json
from tcg.utils.connection_gs import set_credentials_path, authenticate_gs


def insert_values(df):

    path = set_credentials_path()
    with open(path) as file:
        config = json.load(file)

    scope = [config['scope']['feeds'],
             config['scope']['api']]

    data = [df.columns.tolist()] + df.values.tolist()

    client = authenticate_gs(path, scope)
    spreadsheet = client.open(config['sheet']['source'])
    worksheet = spreadsheet.worksheet(config['sheet']['preview'])
    worksheet.update('A1', data)

    return dict(status=200,
                message= 'Updated Successfully')

def save_cache(cat, key, df):
    path = set_credentials_path()
    with open(path) as file:
        config = json.load(file)

    scope = [config['scope']['feeds'],
             config['scope']['api']]

    client = authenticate_gs(path,scope)
    spreadsheet = client.open(config['sheet']['source'])
    worksheet = spreadsheet.worksheet(config['sheet']['cache'])
    fecha_actual = datetime.datetime.now()
    new_row = [
        key,
        cat,
        json.dumps(df),
        fecha_actual.strftime('%Y%m%d')
    ]
    worksheet.append_row(new_row)

