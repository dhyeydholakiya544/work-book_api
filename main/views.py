from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import LatestUpdatesSerializer
from .models import LastestUpdates
@api_view(['GET', 'POST'])
def latestUpdateListAPI(request):
    if request.method == 'POST':
        serializer = LatestUpdatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data':serializer.data,
                'message': 'Latest-Update created successfully.'
            }
            status_code = status.HTTP_201_CREATED
            return Response(data, status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        querySet = LastestUpdates.objects.all()
        serializer = LatestUpdatesSerializer(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def latestUpdateDetailAPI(request, update_id):
    try:
        querySet = LastestUpdates.objects.get(id=update_id)
    except LastestUpdates.DoesNotExist:
        return Response(data={'message': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LatestUpdatesSerializer(querySet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = LatestUpdatesSerializer(querySet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data':serializer.data,
                'message': 'Latest-Update updated successfully.'
            }
            status_code = status.HTTP_200_OK
            return Response(data, status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = LatestUpdatesSerializer(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'data':serializer.data,
                'message': 'Latest-Update updated successfully.'
            }
            status_code = status.HTTP_200_OK
            return Response(data, status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        querySet.delete()
        return Response(data={'message': "Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)