import requests
from .config import api_url_for_btc, api_url_for_ltc
from .models import *
from datetime import datetime
def get_binance_btc_json():
    return requests.get(api_url_for_btc).json()

def get_binance_ltc_json():
    return requests.get(api_url_for_ltc).json()

def create_cryptobtc_obj():
    btc_data = get_binance_btc_json()
    btc = Cryptos.objects.create(name='BTC', price=btc_data['price'], time=datetime.utcnow())
    return btc

def create_ltc_obj():
    ltc_data = get_binance_ltc_json()
    ltc = Cryptos.objects.create(name='LTC', price=ltc_data['price'], time=datetime.utcnow())
    return ltc
    