from tcg.services.search import search_card

def test_search_card():
    cat = 'Yu-Gi-Oh!'
    key = 'Kuriboh'

    result = search_card(cat, key)

    print(result)

test_search_card()
