from rest_framework.views import APIView, Response, status
from .models import *
from .services import get_api_json, create_object_models
from datetime import datetime

class GetCourseBTC(APIView):
    def get(self, request):
        cur_symbol = get_api_json()['price']
        cur_price = create_object_models()
        return Response(data={'symbol':cur_symbol, 'price':cur_price, 'time':datetime.utcnow()}, status=status.HTTP_200_OK)
        
