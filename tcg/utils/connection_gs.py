import json
import os
import google.oauth2.service_account
import gspread
from typing import Tuple
from gspread import Spreadsheet


def authenticate_gs(path: str, scope: list[str]) -> gspread.client.Client:
    creds = google.oauth2.service_account.Credentials.from_service_account_file(path)
    scope_creds = creds.with_scopes(scope)
    return gspread.authorize(scope_creds)


def get_source(scope: list, credentials_path: str, spreadsheet_name: str) -> dict[str, int | str] | Spreadsheet | tuple:
    """
    Autoriza al cliente de Google Sheets y obtiene el archivo de Google Sheets.

    :param scope: Alcance de la autenticación
    :param credentials_path: Ruta al archivo de credenciales
    :param spreadsheet_name: Nombre del archivo de Google Sheets
    :return: Objeto Spreadsheet o un mensaje de error
    """
    try:
        client = authenticate_gs(credentials_path, scope)
        if isinstance(client, Tuple):
            return client  # Retorna el error si no se pudo autenticar

        spreadsheet = client.open(spreadsheet_name)
        return spreadsheet
    except Exception as e:
        return dict(status=500,
                    message=f'Error getting spreadsheet: {e}')


def set_credentials_path() -> str:
    """
    Establece la ruta al archivo de credenciales de Google.

    :return: Ruta del archivo de configuración
    """
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, 'config', 'config.json')
    return config_path

