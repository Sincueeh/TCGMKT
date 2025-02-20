import json
import pandas as pd
from tcg.services.search import search_in_cache


def test_search_cache():
    category = 'Pokemon'
    key = 'Venusaur'

    result = search_in_cache(category,key)
    json_str = result.get('json_data')
    data = json.loads(json_str)
    df = pd.DataFrame(data)
    print(df)
test_search_cache()