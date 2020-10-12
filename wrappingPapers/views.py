from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from wrappingPapers.models import WrappingPaper
from wrappingPapers.serializers import WrappingPaperSerializer
from rest_framework.decorators import api_view, renderer_classes


@api_view(['GET'])
def wrappingPaper_list(request):
    # Query Parameter
    limit = None

    try:
        limit = request.GET.get('limit')
    except ValueError:
        pass

    if limit and limit.isdigit():
        limit = int(limit)

    if request.method == 'GET':
        if not limit:
            wrappingPapers = WrappingPaper.objects.all()
        else:
            wrappingPapers = WrappingPaper.objects.all()[:limit]
        serializer = WrappingPaperSerializer(wrappingPapers, many=True)
        return Response(data=serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def wrappingPaper_detail(request, pk):
    try:
        wrappingPaper = WrappingPaper.objects.get(pk=pk)
    except WrappingPaper.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = wrappingPaperSerializer(wrappingPaper)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WrappingPaperSerializer(wrappingPaper, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        wrappingPaper.delete()
        return Response(status=204)
