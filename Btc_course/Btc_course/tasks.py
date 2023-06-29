from __future__ import absolute_import
from .celery import app
from BTC_crypto.services import *  
from datetime import timedelta
from BTC_crypto.models import *
@app.task(name='update_BTC_and_LTC_every_10_seconds')


def update_BTC_and_LTC_every_10_seconds():
    btc_url = get_binance_btc_json()
    ltc_url = get_binance_ltc_json()
    update_database = Cryptos.objects.create(name='BTC', price=btc_url['price'], time=datetime.utcnow())
    update_database = Cryptos.objects.create(name='LTC', price=ltc_url['price'], time=datetime.utcnow())
    update_database.save()




app.conf.beat_schedule = {
    
    'run_me_every_10_sec':{
        'task':'update_BTC_and_LTC_every_10_seconds',
        'schedule':timedelta(seconds=10),
    }
    
}
