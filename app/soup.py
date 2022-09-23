import json
from bs4 import BeautifulSoup


def make_soup(response):
    soup = BeautifulSoup(response.content, 'html.parser')

    json_ = '{}'
    json_response = json.loads(json_)

    for row in soup.select('tbody tr'):
        row_text = [x.text for x in row.find_all('td')]

        moneda = row_text[0].strip('   ')
        compra = row_text[2].strip('   ')
        venta = row_text[4].strip('   ')

        json_response[moneda] = {
            'Compra': compra,
            'Venta': venta
        }

    json_response_success = {
        "status": "Success",
        "code": "200",
        "data": [
            json_response
        ]
    }

    return json_response_success
