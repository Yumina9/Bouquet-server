from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from flowers.models import Flower
from flowers.serializers import FlowerSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import generics, viewsets
from rest_framework.views import APIView

@api_view(['GET'])
def flower_list(request):
    
    limit =None
    try:
        limit = request.GET.get('limit')
    except ValueError:
        pass

    if limit and limit.isdigit():
        limit= int(limit)

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

class ShopFlowerView(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

class FlowerList(APIView):
    def get(self, request):
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CRATED)
        return Response(serializer.error, status=status.HTTP_400_BAE_REQUESET)

        
class FlowerList(generics.ListCreateAPIView):
    serializer_class = FlowerSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = Flower.objects.all()
        return Flower.objects.all()

# class FlowerDetail
class FlowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer