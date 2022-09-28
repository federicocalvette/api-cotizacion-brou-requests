import requests
import config

def request_brou():
    try:
        response = requests.request("GET", config.URL_BROU) 
    except:
        response = 'Error'
    return response

