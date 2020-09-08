from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from shops.models import Shop
from shops.serializers import ShopSerializer
from rest_framework.decorators import api_view, renderer_classes
from flowers.serializers import FlowerSerializer
from bouquets.serializers import BouquetSerializer

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
        # return JsonResponse(serializer.data, safe=False)

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

        # print(serializer.data)
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
def shop_detail_flowers(request, pk):
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
def shop_detail_bouquets(request, pk):
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
        
