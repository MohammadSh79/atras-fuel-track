from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from User.models import LegalUser, RealUser
from User.permissions import IsUnion
from .serializers import MembersViewSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import authenticate

class DashboardView(APIView):
    permission_classes = [IsAuthenticated, IsUnion]
    
    def get(self, request):
        # Get driver count and send it via serializer
        return Response("Dashboard API View")
    
class MembersView(APIView):
    permission_classes = [IsAuthenticated, IsUnion]

    def get(self, request):
        # Get all members and send it via serializer
        real_users = RealUser.objects.filter(user_ptr=request.user)
        legal_users = LegalUser.objects.filter(user_ptr=request.user)
        
        data = {
            'real_users': real_users,
            'legal_users': legal_users
        }
        serializer = MembersViewSerializer(data)
        return Response(serializer.data)
    
class UnionTokenObtainView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=401)