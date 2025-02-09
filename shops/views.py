
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from shops.models import Shop
from shops.serializers import ShopSerializer
from rest_framework.decorators import api_view, renderer_classes
from flowers.models import Flower
from flowers.serializers import FlowerSerializer
from bouquets.models import Bouquet
from bouquets.serializers import BouquetSerializer
from ribbons.serializers import RibbonSerializer
from wrappingPapers.serializers import WrappingPaperSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def shop_list(request):
    '''
        전체 shop 리스트를 조회합니다.
        URL: http://localhost:8000/shops
    '''
 
    if request.method == 'GET':
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(data=serializer.data, status = 200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def shop_detail(request, pk):

    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShopSerializer(shop)

        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(shop, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        shop.delete()
        return HttpResponse(status=204)

@api_view(['GET'])
def shop_flowers_list(request, pk):
    '''
    가게에 등록된 꽃 데이터 조회
    http://localhost:8000/shop/1/flowers
    '''
    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        query = shop.flower_set.all()
        serializer = FlowerSerializer(query, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def shop_bouquets_list(request, pk):
    '''
    가게에 등록된 꽃다발 데이터 조회
    http://localhost:8000/shop/1/bouquets
    '''
    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return HttpResponse(status=400)

    if request.method =='GET':
        query = shop.bouquet_set.all()
        serializer = BouquetSerializer(query, many=True)
        return Response(serializer.data, status=200)

@api_view(['GET'])
def shop_ribbons_list(request, pk):
    '''
    가게에 등록된 리본 데이터 조회
    http://localhost:8000/shop/1/ribbons
    '''
    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return HttpResponse(status=400)

    if request.method =='GET':
        query = shop.ribbon_set.all()
        serializer = RibbonSerializer(query, many=True)
        return Response(serializer.data, status=200)

@api_view(['GET'])
def shop_wrappingPaper_list(request, pk):
    '''
    가게에 등록된 포장지 데이터 조회
    http://localhost:8000/shop/1/wrappingPapers
    '''
    try:
        shop = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        return HttpResponse(status=400)

    if request.method =='GET':
        query = shop.wrappingpaper_set.all()
        serializer = WrappingPaperSerializer(query, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def shop_flower_detail(request, shops_id, id):
    try:
        flower = Flower.objects.get(shops_id=shops_id, id=id)
    except Flower.DoesNotExist:
        return Response(status=404)
    print(Flower.objects.filter(shops_id=shops_id, id=id))

    if request.method == 'GET':
        serializer = FlowerSerializer(flower)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FlowerSerializer(flower, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        flower.delete()
        return Response(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def shop_bouquet_detail(request, shops_id, id):
    try:
        bouquet = Bouquet.objects.get(shops_id=shops_id, id=id)
    except Bouquet.DoesNotExist:
        return Response(status=404)
    print(Bouquet.objects.filter(shops_id=shops_id, id=id))

    if request.method == 'GET':
        serializer = BouquetSerializer(bouquet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BouquetSerializer(bouquet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bouquet.delete()
        return Response(status=204)
    
class MyShop(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        shop = Shop.objects.get(user=request.user)
        serializer = ShopSerializer(shop)
        return Response(data=serializer.data, status=200)

