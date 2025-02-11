from tcg.services.search import search_card

def test_search_card():
    cat = 'Pokemon'
    key = "Charizard"

    result = search_card(cat, key)

    print(result)

test_search_card()
