from rest_framework import serializers
from .models import Cryptos



class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptos
        exclude = ['id']        