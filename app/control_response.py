import soup
import template_responses


def control(response):
    status = response.status_code
    if response != 'Error':
        if status == 200:
            json_response = soup.make_soup(response)
        elif status == 404:
            json_response = template_responses.JSON_RESPONSE_404
        elif status == 500:
            json_response = template_responses.JSON_RESPONSE_500
        elif status == 503:
            json_response = template_responses.JSON_RESPONSE_503
    else:
        json_response = template_responses.JSON_RESPONSE_X

    return json_response
