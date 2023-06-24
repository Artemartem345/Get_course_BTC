from rest_framework import serializers
from .models import CryptoBTC



class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoBTC
        fields = '__all__'