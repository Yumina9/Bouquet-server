from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Bouquet_order
from .serializers import BouquetOrderSerializer
from django.views.decorators.csrf import csrf_exempt
from shops.models import Shop
from flowers.models import Flower
from bouquets.models import Bouquet

class ShopOrderList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        order = Bouquet_order.objects.filter(shops__user=request.user)
        serializer = BouquetOrderSerializer(order, many=True)
        print("order", order)
        return Response(data=serializer.data, status=200)


class bouquet_order_list(generics.ListCreateAPIView):

    # IsAuthenticated가 있어야만 request.user 사용가능
    permission_classes = [IsAuthenticated]
    queryset = Bouquet_order.objects.all()
    serializer_class = BouquetOrderSerializer

    def perform_create(self, serializer):

        # request.data에는 axios의 post요청에서 담아서 보낸 데이터들 키값으로 그대로 들어오게 되어있어
        flower = Flower.objects.get(id=self.request.data['flower_id']) if self.request.data['flower_id'] else None
        bouquet = Bouquet.objects.get(id=self.request.data['bouquet_id']) if self.request.data['bouquet_id'] else None
        shop = Shop.objects.get(id=self.request.data['shop_id']) if self.request.data['shop_id'] else None
        price = self.request.data['resultPrice'] if self.request.data['bouquet_id'] else 0

        serializer.save(users=self.request.user, shops=shop, bouquet=bouquet, flower=flower, price=price)

class bouquet_order_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bouquet_order.objects.all()
    serializer_class = BouquetOrderSerializer

