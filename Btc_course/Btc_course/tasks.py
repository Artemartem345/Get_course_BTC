from __future__ import absolute_import
from .celery import app
from BTC_crypto.services import *  
from datetime import timedelta
from BTC_crypto.models import *
@app.task(name='update_BTC_every_10_seconds')


def update_BTC_every_10_seconds():
    result = get_api_json()
    update_database = CryptoBTC.objects.create(name='BTC', price=result['price'], time=datetime.utcnow())
    update_database.save()




app.conf.beat_schedule = {
    
    'run_me_every_10_sec':{
        'task':'update_BTC_every_10_seconds',
        'schedule':timedelta(seconds=10),
        
        
    }
    
}
