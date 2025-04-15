from tcg.services.retrieve import get_sheets

def test_get_result():
    worksheet = get_sheets()

    print(worksheet.get_all_records())

test_get_result()