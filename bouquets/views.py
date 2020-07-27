from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from bouquets.models import Bouquet
from bouquets.serializers import BouquetSerializer 
from rest_framework.decorators import api_view, renderer_classes

@api_view(['GET'])
def bouquet_list(request):
    if request.method == 'GET':
        bouquets = Bouquet.objects.all()
        serializer = BouquetSerializer(bouquets, many=True)
        return Response(data=serializer.data, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BouquetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def bouquet_detail(request, pk):
    try:
        bouquet = Bouquet.objects.get(pk=pk)
    except Bouquet.DoesNotExist:
        return Response(status=404)

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