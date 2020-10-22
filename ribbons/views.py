from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ribbons.models import Ribbon
from ribbons.serializers import RibbonSerializer
from rest_framework.decorators import api_view, renderer_classes

@api_view(['GET'])
def ribbon_list(request):
    limit = None

    try:
        limit = request.GET.get('limit')
    except ValueError:
        pass

    if limit and limit.isdigit():
        limit = int(limit)

    if request.method == 'GET':
        if not limit:
            ribbons = Ribbon.objects.all()
        else:
            ribbons = Ribbon.objects.all()[:limit]
        serializer = RibbonSerializer(ribbons, many=True)
        return Response(data=serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def ribbon_detail(request, pk):
    try:
        ribbon = Ribbon.objects.get(pk=pk)
    except Ribbon.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = RibbonSerializer(ribbon)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RibbonSerializer(ribbon, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ribbon.delete()
        return Response(status=204)
