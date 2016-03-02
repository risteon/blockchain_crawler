import json
import requests

URL_LATEST_BLOCK = 'https://blockchain.info/latestblock'


def get_latest_block():
    response = requests.get(url=URL_LATEST_BLOCK)
    return json.loads(response.text)
