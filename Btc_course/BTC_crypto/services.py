import requests
from .config import api_url
from .models import *
from datetime import datetime
def get_binance_btc_json():
    return requests.get(api_url).json()

def create_cryptobtc_obj():
    btc_data = get_binance_btc_json()
    btc = CryptoBTC.objects.create(name='BTC', price=btc_data['price'], time=datetime.utcnow())
    return btc