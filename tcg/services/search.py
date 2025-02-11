import requests
from bs4 import BeautifulSoup

from tcg.services.insert import insert_values
from tcg.services.scrap import html_scrap


def search_card(category, key):
    try:
        if category == 'Pokemon':
            num = '7061'
        else:
            num = '4736'

        url_template = ('https://www.trollandtoad.com/category.php?'
                        f'selected-cat={num}&search-words={key}&'
                        'token=pFD1L2jASwaEyIFQbVsSLCoaGLW7wJWYem'
                        '%2Bfi273PlTXlmeSzrZPCrrgekiS8Rt54bpq2F2XGGL7RVm0GiPV7A%3D%3D')

        web = requests.get(url_template)
        web.raise_for_status() #HTTP Errors

        bp = BeautifulSoup(web.text, 'html.parser')
        df = html_scrap(category, bp)
        response = insert_values(df)

        return response
    except requests.RequestException as re:
        return dict(status=404,
                    message=f'Unreachable. {re}')