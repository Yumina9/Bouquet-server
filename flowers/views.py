from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from flowers.models import Flower
from flowers.serializers import FlowerSerializer
from rest_framework.decorators import api_view, renderer_classes


@api_view(['GET'])
def flower_list(request):
 
    if request.method == 'GET':
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(data=serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FlowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def flower_detail(request, pk):
    try:
        flower = Flower.objects.get(pk=pk)
    except Flower.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FlowerSerializer(flower)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FlowerSerializer(flower, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        flower.delete()
        return HttpResponse(status=204)