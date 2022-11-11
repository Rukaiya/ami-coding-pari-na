from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User

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
    paginator = PageNumberPagination()
    paginator.page_size = 30
    paginator.max_page_size = 100
    
    # if user is present then perform query
    try:
        user = User.objects.get(pk=user_id)
        khojes = user.khoj_set.filter(created_at__range=[start_datetime, end_datetime])
        khojes = paginator.paginate_queryset(khojes, request)
        serializer = KhojSerializer(khojes, many=True).data
    except User.DoesNotExist:
        user = None
        serializer = 'User not Found'
    
    return Response({'status': status, 'user_id': user_id, 'payload': serializer})
    