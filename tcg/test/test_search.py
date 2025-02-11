from tcg.services.search import search_card

def test_search_card():
    cat = 'Pokemon'
    key = "Pidgeot"

    result = search_card(cat, key)

    print(result)

test_search_card()
