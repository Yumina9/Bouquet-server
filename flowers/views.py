from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from flowers.models import Flower
from flowers.serializers import FlowerSerializer
from rest_framework.decorators import api_view, renderer_classes


@api_view(['GET'])
def flower_list(request):
    
    limit =None
    try:
        limit = request.GET.get('limit',None)
    except ValueError:
        pass

    if limit.isdigit():
        limit= int(limit)
    else:
        limit = None

    if request.method == 'GET':
        if not limit:
            flowers = Flower.objects.all()
        else:
            flowers = Flower.objects.all()[:limit]
        serializer = FlowerSerializer(flowers, many=True)
        return Response(data=serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def flower_detail(request, pk):
    try:
        flower = Flower.objects.get(pk=pk)
    except Flower.DoesNotExist:
        return Response(status=404)

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