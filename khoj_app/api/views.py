from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils.timezone import make_aware

from .serializers import KhojSerializer
from khoj_app.models import Khoj

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getKhojes(request):
    serializer = ''
    status = 'success'
    user_id = request.GET.get('user_id')
    start_datetime = request.GET.get('start_datetime')
    end_datetime = request.GET.get('end_datetime')
    
    # if user is present then perform query
    try:
        user = User.objects.get(pk=user_id)
        khojes = user.khoj_set.filter(created_at__range=[start_datetime, end_datetime])
        serializer = KhojSerializer(khojes, many=True).data
        print(serializer)
    except User.DoesNotExist:
        user = None
        serializer = 'User not Found'
    
    return Response({'status': status, 'user_id': user_id, 'payload': serializer})
    