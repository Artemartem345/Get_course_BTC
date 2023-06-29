from rest_framework.views import APIView, Response, status
from .models import *
from .services import *
from .serializers import * 


class GetCourseBTC(APIView):
    def get(self, request):
        btc = create_cryptobtc_obj()
        serializer = CurrencySerializer(btc)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
class GetCourseLTC(APIView):
    def get(self, request):
        ltc = create_ltc_obj() 
        serializer = CurrencySerializer(ltc)
        return Response(data=serializer.data, status=status.HTTP_200_OK)