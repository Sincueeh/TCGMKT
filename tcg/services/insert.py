import datetime
import json
from tcg.utils.connection_gs import set_sheet


def insert_values(df):

    data = [df.columns.tolist()] + df.values.tolist()

    worksheet = set_sheet(0)
    worksheet.update('A1', data)

    return dict(status=200,
                message= 'Updated Successfully')

def save_cache(cat, key, df):

    try:
        worksheet = set_sheet(1)
        fecha_actual = datetime.datetime.now()
        new_row = [
            cat,
            key,
            json.dumps(df),
            fecha_actual.strftime('%Y%m%d')
        ]
        worksheet.append_row(new_row)

        return dict(status=200, message='Success')
    except Exception as e:
        return dict(status=500, message=f'Failed {e}')

