import requests
from .config import api_url
from .models import *
from datetime import datetime
def get_api_json():
    url_json = requests.get(api_url)
    data_json = url_json.json()
    
    return data_json

def create_object_models():
    url_json = requests.get(api_url)
    data_json = url_json.json()
    CryptoBTC.objects.create(name='BTC', price=data_json['price'], time=datetime.utcnow())
    return data_json

