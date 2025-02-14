import uuid
import pandas

def html_scrap(category, html):
    names = []
    images = []
    expansions = []
    prices = []

    try:
        cards = html.find_all(class_='card-text')
        for card in cards:
            name = card.get_text(separator=" ", strip=True)
            names.append(name)

        divs = html.find_all('div', {'class': 'prod-img-container'})
        for div in divs:
            tag = div.find('img')
            if tag and 'data-src' in tag.attrs:
                img = tag['data-src']
                images.append(img)

        prod_cat = html.find_all('div', class_='prod-cat')
        for exp_div in prod_cat:
            exp = exp_div.find('a')
            if exp:
                expansions.append(exp.get_text(strip=True))
            else:
                expansions.append('N/A Single')

        info = html.find_all('div', class_=[
            'col-2 text-center p-1',
            'font-smaller font-weight-bold text-sm-center pr-2 text-info'
        ])
        for txt in info:
            price = txt.get_text(strip=True)
            if price.startswith('$'):
                prices.append(price.replace('$', ''))

        length = min(len(names), len(images),
                     len(expansions), len(prices))
        min_list = []
        for i in range(length):
            new_uuid = str(uuid.uuid4())
            min_list.append((
                new_uuid,
                names[i],
                expansions[i],
                prices[i],
                images[i],
                category
            ))

        df = pandas.DataFrame(min_list, columns=['uuid', 'Card',
                                                 'Expansion', 'Price',
                                                 'Image', 'Type'])

        return df

    except Exception as e:
        return dict(status=400,
                    message=f'Unable to retrieve list. {e}')
