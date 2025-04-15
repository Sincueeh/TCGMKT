import json
import gspread
from flask import jsonify, request
from functions_framework import http
from tcg.utils.connection_gs import set_credentials_path
from google.oauth2.service_account import Credentials

CREDENTIALS_PATH= set_credentials_path()
with open(CREDENTIALS_PATH) as file:
    config = json.load(file)

SCOPES= [config['scope']['feeds'], config['scope']['api']]
SHEET= config['sheet']['source']
CACHE= config['sheet']['cache']

def get_sheets():

    creds = Credentials.from_service_account_info(config)
    scoped_creds = creds.with_scopes(SCOPES)
    client = gspread.authorize(scoped_creds)
    spreadsheet = client.open(SHEET)
    worksheet = spreadsheet.worksheet(CACHE)

    return worksheet

