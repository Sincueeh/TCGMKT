import json

from tcg.utils.connection_gs import set_credentials_path, authenticate_gs


def insert_values(df):
    try:
        path = set_credentials_path()
        with open(path) as file:
            config = json.load(file)

        scope = [config['scope']['feeds'],
                 config['scope']['api']]

        data = [df.columns.tolist()] + df.values.tolist()

        client = authenticate_gs(path, scope)
        spreadsheet = client.open(config['sheet']['source'])
        worksheet = spreadsheet.worksheet('Test')
        worksheet.update('A1', data)

        return dict(status=200,
                    message= 'Updated Successfully')

    except Exception as e:
        return dict(status=500,
                    message=f'Failed to insert. {e}')
