from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from flowers.models import Flower
from flowers.serializers import FlowerSerializer

@csrf_exempt
def flower_list(request):
 
    if request.method == 'GET':
        flowers = Snippet.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return JsonResponse(serializer.data, safe=False)

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