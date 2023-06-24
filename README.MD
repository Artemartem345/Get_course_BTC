# Get course BTC from Binance API CryptoCurrencyExchange 


## Techology stack
- python3 3.10.6
- Django==4.2.2
- django-restframework==0.0.1
- celery, redis(Broker) == 5.3.1, 4.5.5 



### For start:
- python manage.py runserver
- celery -A Btc_course beat -l info
- launch worker -> celery -A < Name folder with settings.py > worker -l info
- Enjoy! you will get actual course BTC from binance every 10 seconds!